#Third party apps
from rest_framework import serializers
#Models
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
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