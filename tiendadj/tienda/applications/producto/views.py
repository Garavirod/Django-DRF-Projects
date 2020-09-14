# Third party app
from rest_framework.generics import (
    ListAPIView,
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


class ListProductByUserView(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all()
    



