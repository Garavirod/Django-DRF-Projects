# third patty apps
from rest_framework import serializers

# Models
from .models import (
    Sale,
    SaleDetail
)

# Django

""" Serializer that shows all sales and its detail """
class SaleReportSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField() # foreign object
    class Meta:
        model = Sale
        fields = (
            'date_sale',
            'amount',
            'count',
            'cancelado',
            'state',
            'adreese_send',
            'anulate',
            'user',   
            'product', # foreign object to serialize         
        )
    """ 'obj' represents each object in json """
    def get_product(Self, obj):
        query = SaleDetail.objects.products_by_sale(obj.id)
        # serielizing each object using other serializer using many because are more of one
        serialized_query = DetailSerializer(query, many=True).data #object is inside of '.data'
        return serialized_query

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = ('__all__')



class ProductDetailSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    count = serializers.IntegerField()

"""
    Serialize a sale in process
    This is the structure Fronted developer should send data
"""
class ProcessSaleSerializer(serializers.Serializer):
    type_invoce =  serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    product = ProductDetailSerializer(many=True) # Many serialized products 
