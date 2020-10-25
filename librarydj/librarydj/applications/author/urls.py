from django.contrib import admin
from django.urls import path
# Views
from . import views

urlpatterns = [
    path(
        'authors/', 
        views.ListAuthors.as_view(), 
        name="authors"
    ),
]
