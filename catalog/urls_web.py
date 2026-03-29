from django.urls import path
from . import views

urlpatterns = [
    path("", views.web_home, name="web_home"),
    path("profile/", views.web_profile, name="web_profile"),
    path("books/", views.web_books, name="web_books"),
    path("category/<slug:slug>/", views.web_category, name="web_category"),
    path("books/<int:book_id>/", views.web_book_detail, name="web_book_detail"),
    path("favorites/", views.web_favorites, name="web_favorites"),
]