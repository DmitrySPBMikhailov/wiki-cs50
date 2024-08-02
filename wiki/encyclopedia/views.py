from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


# Show encyclopedia entry
def show_entry(request, title):
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/404_mistake.html", {"title": title})
    markdowner = Markdown()
    entry = markdowner.convert(entry)
    context = {"entry": entry, "title": title}
    return render(request, "encyclopedia/one_entry.html", context)


# Search encyclopedia entry
def search_entry(request):
    title = request.POST["q"]
    if util.get_entry(title):
        return redirect(f"/wiki/{title}/")
    else:
        all_entries = util.list_entries()
        matching_entries = []
        for all in all_entries:
            if title.upper() in all.upper():
                matching_entries.append(all)
        context = {"matching_entries": matching_entries}
        return render(request, "encyclopedia/show_search_results.html", context)


# Create new encyclopedia entry
def create_entry(request):
    page_action = "Create a new entry"
    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]
        # Check if title exists
        if util.get_entry(title):
            return render(
                request, "encyclopedia/entry_already_exists.html", {"title": title}
            )
        util.save_entry(title, content)
        return redirect(f"/wiki/{title}/")
    context = {"page_action": page_action}
    return render(request, "encyclopedia/create_entry.html", context)


# Edit encyclopedia entry
def edit_entry(request, title):
    page_action = "Edit"
    # Fill the form
    description = util.get_entry(title)
    # markdowner = Markdown()
    # description = markdowner.convert(description)
    if request.POST:
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect(f"/wiki/{title}/")
    context = {"page_action": page_action, "title": title, "description": description}
    return render(request, "encyclopedia/edit_entry.html", context)


# Random page
def choose_random(request):
    all_entries = util.list_entries()
    all_entries_count = len(all_entries)
    random_num = random.randint(0, all_entries_count - 1)
    return redirect(f"/wiki/{all_entries[random_num]}/")
