import datetime
from django.db import models

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