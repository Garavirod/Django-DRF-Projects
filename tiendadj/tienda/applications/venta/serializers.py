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



"""
    This serializeer is used for deserializyng an object which 
    data has Object structure 
    {
        pk: 1,
        count:2,
    }  
"""
class ProductDetailSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    count = serializers.IntegerField()


""" 
    This serializeer is used for deserializyng an object which 
    data has Array structure 

"""

class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField() #This represent an array of integers


"""
    Serialize a sale in process
    This is the structure Fronted developer should send data
"""
class ProcessSaleSerializer(serializers.Serializer):
    type_invoce =  serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    product = ProductDetailSerializer(many=True) # Many serialized products 



"""
    This serializer is used when an atribute is an array 
    instead ann object Json
"""
class ProcessSaleSerializerV2(serializers.Serializer):
    type_invoce =  serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    product = ArrayIntegerSerializer()
    quantities = ArrayIntegerSerializer()

    """VIEWSETS VALIDATIONS"""

    # data is the whole set of atributtes
    def validate(sel,data):
        if not data['type_payment'] in ['0','1','2']:
            raise serializers.ValidationError('Please, set a correct type of payment')
        return data

    # 'Value' is an item that in execution time is been asigened to 'type_invoce'
    def validate_type_invoce(self,value):
        if not value in ['0','3','4']:
            raise serializers.ValidationError('Please, set a correct value')
        return value