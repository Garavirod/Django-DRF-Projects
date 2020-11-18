from django.contrib import admin
from django.urls import path
# Views
from . import views

urlpatterns = [
    path(
        'books/', 
        views.ListBookView.as_view(), 
        name="books"
    ),
    path(
        'books-trg/', 
        views.ListBookViewTrigram.as_view(), 
        name="books-trg"
    ),
    path(
        'books/category', 
        views.ListBookCategory.as_view(), 
        name="books-cat"
    ),
    path(
        'books/category-author', 
        views.ListBookCategoryAuthor.as_view(), 
        name="books-cat-author"
    ),    
    path(
        'books/detail/<pk>/', 
        views.BookDetailView.as_view(), 
        name="books-detail"
    )
]
