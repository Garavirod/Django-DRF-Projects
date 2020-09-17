from django.db import models


class SaleDetailManager(models.Manager):
    def products_by_sale(self, venta_id):
        query = self.filter(
            sale__id= venta_id,
        ).order_by('count','product__name')
        return query
