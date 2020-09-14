# Third party app
from rest_framework.generics import (
    ListAPIView,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Serializer
from .serializers import (
    ProductSerializer,
)

# Django
from django.shortcuts import render

# Models

from .models import (
    Product,
)


class ListProductByUserView(ListAPIView):
    """
        Override 
    """
    serializer_class = ProductSerializer    
    # Through TokenAuthentication from REST FR.. identify and figure out token's user
    authentication_classes = (TokenAuthentication,)
    # This line does not allow any user who isn't authenticated
    permission_classes = [IsAuthenticated] #Permisson based in previus authentication
    def get_queryset(self):
        _user = self.request.user # getting user
        return Product.objects.products_by_user(_user) #Custom filter
    



