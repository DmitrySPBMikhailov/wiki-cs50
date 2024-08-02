from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.show_entry, name="show_entry"),
    path("create/", views.create_entry, name="create_entry"),
    path("edit/<str:title>", views.edit_entry, name="edit_entry"),
    path("search/", views.search_entry, name="search_entry"),
    path("search-results/", views.search_entry, name="search_entry"),
    path("choose-random/", views.choose_random, name="choose_random"),
]
