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

    def searchAuthorExcludeByAge(self,author_name):
        result = self.filter(
            Q(name__icontains=author_name) | Q(surname__icontains=author_name)
        )
        result = result.exclude(age=60)
        return result

    # <= or >= 
    def searchAuthorv5(self):
        result = self.filter(
            age__gt=40, #gratest than a comma references a logical 'and'
            age__lt=60 #Lowest than
        )
        result = result.order_by('surname','name')
        return result