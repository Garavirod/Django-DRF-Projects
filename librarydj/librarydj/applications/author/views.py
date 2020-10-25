from django.shortcuts import render
from django.views.generic import ListView
# Models
from .models import Author

class ListAuthors(ListView):    
    context_object_name = "authors_list" #object that is shared in a template
    template_name = "author/author_list.html"
    
    def get_queryset(self):
        author_name = self.request.GET.get("author_name","")
        # return Author.object_manager.getAuthorsList()
        # return Author.object_manager.searchAuthor(author_name)
        return Author.object_manager.searchAuthorByFullName(author_name)
    
    

