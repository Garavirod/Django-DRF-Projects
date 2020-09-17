# Third partty apps
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
)

# Django
from django.shortcuts import render

# Serializers
from . import serializers

# Models

from .models import (
    Sale,
    SaleDetail
)


class SaleReportView(ListAPIView):
    serializer_class = serializers.SaleReportSerializer
    def get_queryset(self):
        return Sale.objects.all()
    
class RegisterSaleView(CreateAPIView):
    # Authetication verify
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        IsAuthenticated, #if is authenticated     
    ] 

    # using serializer 
    serializer_class = serializers.ProcessSaleSerializer

    """
        CreateView is a generic view based in post request HTTP,
        this creates an instance in @param{request} when request is sent
    """

    # override
    def create(self,request,*args, **kwargs):
        """ 
            deserializing data from http (POST)
            It is recived data in a json fromat and 'ProcessSaleSerializer' 
            deserialize that infromation
        """ 
        _serialized_data = serializers.ProcessSaleSerializer(data=request.data)

        #Verify if data structue is correct
        _serialized_data.is_valid(raise_exception=True)

        # Access to data previosly validated

        tipo_recibo = _serialized_data.validated_data['type_invoce']