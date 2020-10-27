from django.shortcuts import render
from django.views.generic import ListView

# Models
from .models import Book, Category
# Create your views here.

class ListBookView(ListView):
    context_object_name = "books_list" #object that is shared in a template
    template_name = "book/book_list.html"

    def get_queryset(self):
        # Book title
        title_book = self.request.GET.get("kword","")
        # date range
        date_1 = self.request.GET.get("date1","")
        date_2 = self.request.GET.get("date2","")

        if date_1 and date_2:
            return Book.object_manager.BookList(title_book,date_1,date_2)
        else:
            return Book.object_manager.BookListAll(title_book)

class ListBookCategory(ListView):
    context_object_name = "book_list_category" #object that is shared in a template
    template_name = "book/book_category_list.html" #Template
    # Category
    def get_queryset(self):
        category = '3'
        return Book.object_manager.BookListByCategory(category)
    


class ListBookCategoryAuthor(ListView):
    context_object_name = "books_category_auth" #object that is shared in a template
    template_name = "category/books_category_auth.html" #Template
    # Category
    def get_queryset(self):
        author = '2'
        return Category.object_manager.categoryByAuthor(author)
