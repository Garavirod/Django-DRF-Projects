from django.db import models

# Managers
from .managers import AuthorManager

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

    # Connect the manager
    object_manager = AuthorManager()

    def __str__(self):
        return str(self.id) + " - " + self.name + " " + self.surname
    
