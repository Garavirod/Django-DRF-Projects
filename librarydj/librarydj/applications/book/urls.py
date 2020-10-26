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
]
