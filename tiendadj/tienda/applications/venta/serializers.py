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
        )
