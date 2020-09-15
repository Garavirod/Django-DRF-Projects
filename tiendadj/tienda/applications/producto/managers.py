from django.db import models

class ProductManager(models.Manager):
    def products_by_user(self,_user):
        return self.filter(
            user_created=_user
        )
    def products_with_stock(self):
        return self.filter(
            stok__gt=0
        ).order_by('-num_sales') #agrupado por num de ventas en orden inverso

    def product_by_gender(self, gender):    
        # Evaluating param
        if gender == 'm':
            mujer = True
            varon = False
        elif gender=='v':
            mujer = False
            varon = True
        else:
            mujer = True
            varon = True
        # Filtter by gender
        return self.filter(
            woman=mujer,
            man=varon    
        )

    def filter_products(self,**filters): # **filters many params
        return self.filter(
            man=filters['man'],
            woman=filters['woman'],
            name__icontains=filters['name'],
        )
