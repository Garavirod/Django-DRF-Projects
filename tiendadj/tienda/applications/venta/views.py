# Third partty apps
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
)

# Django
from django.shortcuts import render
from django.utils import timezone

# Serializers
from . import serializers

# Sale Models
from .models import (
    Sale,
    SaleDetail,
)

# Product Model
from applications.producto.models import Product


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
            deserialize that infromation,
            In brief, the frontend send infromation in a JSON fromat
        """ 
        _serialized_data = serializers.ProcessSaleSerializer(data=request.data)

        #Verify if data structue is correct
        _serialized_data.is_valid(raise_exception=True)

        # Access to data previosly validated
        # tipo_recibo = _serialized_data.validated_data['type_invoce']


        # This register a sale in BDD acordding to serializer structure
        _sale = Sale.objects.create(
            date_sale= timezone.now(),
            amount=0,
            count=0,
            type_invoce=_serialized_data.validated_data['type_invoce'],
            type_payment=_serialized_data.validated_data['type_payment'],
            adreese_send=_serialized_data.validated_data['adreese_send'],
            user=self.request.user,
        )

        # Getting sale's products in the register
        productos = _serialized_data.validated_data['product']

        # for each product in the sale wecreate a sale detail object
        sales_details = []
        _amount = 0
        _count = 0

        for producto in productos:
            p = Product.objects.get(id=producto['pk']) #getting the product
            # Obje type sale detail 
            sale_detail = SaleDetail(
                sale=_sale, # sale previously registered
                product=p,
                count=producto['count'],
                price_purchase=p.price_purchase,
                price_sale=p.price_sale
            )
            #Adding up the amount
            _amount += _amount + p.price_sale*producto['count']
            _count += _count + producto['count']

            #Setting the total amount to Object Sale
            _sale.amount = _amount
            _sale.count = _count

            #Saving the data in Sale
            _sale.save()

            # Adding sale datil to list of sales detail
            sales_details.append(sale_detail)

        #Bulk create for save Sale detaisl of ech product
        SaleDetail.objects.bulk_create(sales_details)

        return Response({'success':'sale was registered successful'})