from django.db import models
from applications.book.models import Book
# Create your models here.
class Reader(models.Model):
    name = models.CharField(
        max_length=50
    )

    surname = models.CharField(
        max_length=50
    )

    nacionality = models.CharField(
        max_length=30
    )

    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name + " " + self.surname



class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book,on_delete=models.CASCADE,
        related_name='borrowing'

    )
    loan_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    is_returned = models.BooleanField()

    def __str__(self):
        return self.book.title
    