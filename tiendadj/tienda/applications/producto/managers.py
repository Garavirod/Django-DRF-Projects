from django.db import models

class ProductManager(models.Manager):
    def products_by_user(self,_user):
        return self.filter(
            user_created=_user
        )
