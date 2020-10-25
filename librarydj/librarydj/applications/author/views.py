from django.shortcuts import render
from django.views.generic import ListView
# Models
from .models import Author

class ListAuthors(ListView):    
    context_object_name = "authors_list"
    template_name = "author/author_list.html"
    

