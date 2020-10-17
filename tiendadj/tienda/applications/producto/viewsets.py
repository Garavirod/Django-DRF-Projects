# third party apps
from rest_framework import viewsets
from rest_framework.response import Response
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

    # Perfomed created is a function that can be override to handy data before date be created    
    def perform_create(self,serializer):
        # chanege data's serializer in performane, acordin to a model
        serializer.save(
            video="https://www.youtube.com/watch?v=gxRq23qVE8A"
        )

    def list(self,request,*args, **kwargs):
        queryset = Product.objects.products_by_user(self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Override method create
    # def create(self,request):
    #     # Request data is data that just been created
    #     print(request.data)

    #     return Response(
    #         {
    #             'code':'ok'
    #         }
    #     )

