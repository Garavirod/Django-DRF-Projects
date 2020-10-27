from django.db import models
from applications.author.models import Author

# Managers
from .managers import BookManager
# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=30)
    def __str__(self):
        return str(self.id) + " - " + self.name_category
    

class Book(models.Model):    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)    
    title = models.CharField(max_length=50)
    date = models.DateField('Launch date')
    cover_page = models.ImageField(upload_to="cover_page")
    views = models.PositiveIntegerField()
    # Manager connection
    object_manager = BookManager()

    def __str__(self):
        return self.title
    
