# Third partty apps
from rest_framework.generics import (
    ListAPIView,
)

# Django
from django.shortcuts import render

# Serializers
from . import serializers

# Models

from .models import (
    Sale,
)


class SaleReportView(ListAPIView):
    serializer_class = serializers.SaleReportSerializer
    def get_queryset(self):
        return Sale.objects.all()
    