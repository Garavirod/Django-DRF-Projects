from django.db import models
from django.db.models import Count


"""
    In this file goes all queries
"""

class MeetingManager(models.Manager):
    def count_meetings(self):
        result = self.values('person__job').annotate(
            cantidad=Count('id') #new atributes in the data don't forget add a new serializer with this characteristic
        )
        return result