import datetime
from django.db import models
from django.db.models import Q, Count

class BookManager(models.Manager):

    def BookListAll(self,kword):
        result = self.filter(
            title__icontains=kword,
            date__range=('2000-01-01','2020-12-12')
        )
        return result

    def BookList(self,kword,date1,date2):
        d1 = datetime.datetime.strptime(date1,'%Y-%m-%d').date()
        d2 = datetime.datetime.strptime(date2,'%Y-%m-%d').date()
        result = self.filter(
            title__icontains=kword,
            date__range=(d1,d2)
        )
        return result

    def BookListByCategory(self,cat):
        result = self.filter(
            # Model1Attr__Model2Attr(FK:atribute) or id if you want a unique identifier
            category__id=cat
        ).order_by('title')

        return result

    def AddNewAuthorToBook(self,book_id,author):
        book = self.get(id=book_id)
        book.author.add(author)
        return book

    def RemoveAuthorToBook(self,book_id,author):
        book = self.get(id=book_id)
        book.author.remove(author)
        return book

class CategoryManager(models.Manager):
    def categoryByAuthor(self,author):
        """
            Model CategoryModel access to Book through 'category_book'
            Book access to AuthorModel thorugh 'author' to arrive id
        """
        # Find categories
        result = self.filter(
            category_book__author__id=author
        )
        # exclude repetitive items
        result = result.distinct()
        # Order by category name
        result = result.order_by('name_category')
        return result


    """
        This query brings all categories including the number of books
        that it has got.

        cat1 - cat.name  - numbooks
    """
    def ListCategoryBook(self):
        result = self.annotate(
            num_books =  Count('category_book') #count bum of  book that has got each category
        )

        for r in result:
            print("******")
            print(r, r.num_books)
        return result