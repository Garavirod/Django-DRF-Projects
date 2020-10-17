#Third party apps
from rest_framework import serializers, pagination
#Models
from .models import Product, Colors


# COLORS

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = (
            'color',
        )



# PRODUCT
class ProductSerializer(serializers.ModelSerializer):

    # Redefinig the atribute colors with other serializer, 'many=True' beacuse of are more than one
    colors = ColorSerializer(many=True)

    # Connect the model
    class Meta:
        model = Product
        # Fields that the serializer will show in Json
        fields = (
            'name',
            'description',
            'man',
            'woman',
            'weight',
            'price_purchase',
            'price_sale',
            'main_image',
            'image1',
            'image2',
            'image3',
            'colors',
            'video',
            'stok',
            'num_sales',
            'user_created',            
        )


class ProductSerializerAll(serializers.ModelSerializer):
    # Connect the model
    class Meta:     
        model = Product   
        # Fields that the serializer will show in Json
        fields = ('__all__')




# Pagination

class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 5
    max_page = 50    