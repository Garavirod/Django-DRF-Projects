from django.db import models
from django.db.models import Count, Avg, Sum

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