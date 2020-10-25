from django.db import models

# Create your models here.
class Author(models.Model):
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
    
