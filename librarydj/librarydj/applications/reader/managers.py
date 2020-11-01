from django.db import models
from django.db.models import Count, Avg, Sum
from django.db.models.functions import Lower

class LoanManagrer(models.Manager):
    """
        Age average people who reads a book
    """
    def AverageReaderBook(self):
        result=self.filter(
            book__id = '1' #All the Book's borrowings 
        ).aggregate(
            avg_age = Avg('reader__age'),
            sum_age = Sum('reader__age')
        )
        return result

    def NumBorrowingsByBook(self):
        """
            In the model Loan, condider the atribute  values('book'),
            and count how many times is in the table Loan:
            annoante(.....book)
        """
        result=self.values( #here goes a parametter of agrupation
            'book'
        ).annotate(
            num_borrowings=Count('book'),
            title=Lower('book__title')
        )

        for r in result:
            print(r, r['num_borrowings'])
        
        return result

    def NumBorrowingsByUser(self):
        """
            How many times a book has been borrowed groped by reader
        """
        result=self.values( #here goes a parametter of agrupation
            'book',
            'reader'
        ).annotate(
            num_borrowings=Count('book'),
            title=Lower('book__title')
        )

        for r in result:
            print(r, r['num_borrowings'])
        
        return result