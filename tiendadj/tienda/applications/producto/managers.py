from django.db import models

class ProductManager(models.Manager):
    def products_by_user(self,_user):
        return self.filter(
            user_created=_user
        )
    def products_with_stock(self):
        return self.filter(
            stok__gt=0
        ).order_by('-num_sales')