from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.api_profile, name="api_profile"),
    path("books/", views.api_books, name="api_books"),
    path("category/<slug:slug>/", views.api_category, name="api_category"),
    path("books/<int:book_id>/", views.api_book_detail, name="api_book_detail"),
    path("favorites/", views.api_favorites, name="api_favorites"),
    path("favorites/add/", views.api_add_favorite, name="api_add_favorite"),
    path("favorites/remove/", views.api_remove_favorite, name="api_remove_favorite"),
]