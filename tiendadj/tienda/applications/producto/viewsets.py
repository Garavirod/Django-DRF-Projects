# third party apps
from rest_framework import viewsets
# models
from .models import Colors, Product
# Serializers
from .serializers import (
    ColorSerializer, 
    ProductSerializerAll,
    PaginationSerializer
)

"""
    CRUD with a viewset, don't forget to create the router.py 
    for using the viewset, this is for havingmor order in the project
"""
class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    # Override params
    queryset = Colors.objects.all()

"""
    Viewset para el serializador Prouctoserializer
"""
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializerAll
    # Override params
    queryset = Product.objects.all()
    # Add a pagination class
    pagination_class = PaginationSerializer


