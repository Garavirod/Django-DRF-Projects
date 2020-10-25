from django.db import models
from django.db.models import Q #For querys Or type

class AuthorManager(models.Manager):
    """Author's manager"""

    def getAuthorsList(self):
        # Where 'self represents the Model.objects'
        return self.all()

    def searchAuthor(self,author_name):
        result = self.filter(
            name__icontains=author_name #is contains an object similar
        )
        return result

    def searchAuthorByFullName(self,author_name):
        result = self.filter(
            Q(name__icontains=author_name) | Q(surname__icontains=author_name)
        )
        return result