# Third party app
from rest_framework.generics import (
    ListAPIView,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
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

"""
    Getting product that are asociated some user
"""
class ListProductByUserView(ListAPIView):
    """
        Override 
    """
    serializer_class = ProductSerializer    
    # Through TokenAuthentication from REST FR.. identify and figure out token's user
    authentication_classes = (TokenAuthentication,)
    # This line does not allow any user who isn't authenticated
    permission_classes = [
        IsAuthenticated,
        # IsAdminUser, just allow access if user is Super user or Admin
        # ReadOnly, Reading permissions only
    ] #Permisson based in previus authentication
    def get_queryset(self):
        _user = self.request.user # getting user
        return Product.objects.products_by_user(_user) #Custom filter
    


class ListProductStok(ListAPIView):
    """
        Override 
    """
    serializer_class = ProductSerializer    

    """
        line below only very if a token exist 
        or belong some user, (ONLY VERIFY)
    """
    
    authentication_classes = (TokenAuthentication,)
    """
        Line below means:
        If exist some user with that token then, 
        you can show the view based in that authentication with
        folowing restrictions.

            1) IsAuthenticated 
            2) ReadOnly..
            etc..

    """
    permission_classes = [
        IsAuthenticated, #if is authenticated
        IsAdminUser, #and if is Super admin
    ] 

    # This view dependes on permission_classes 
    def get_queryset(self):
        return Product.objects.products_with_stock() #Custom filter


"""
    Filtering a product by gender
"""
class ListProductByGender(ListAPIView):
    serializer_class = ProductSerializer    
    def get_queryset(self):
        # Catching param
        _gender = self.kwargs['gender']
        return Product.objects.product_by_gender(_gender)
    
"""
    Using query params with multimple params in request http GET 
"""

class ListProductsFilter(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        # None beacuse of it is posible recieve more params
        varon = self.request.query_params.get('man', None) 
        mujer = self.request.query_params.get('woman',None)
        nombre = self.request.query_params.get('name',None)
        return Product.objects.filter_products(
            man = varon,
            woman = mujer,
            name = nombre,
        );
    