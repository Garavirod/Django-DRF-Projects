# third party apps
from rest_framework import viewsets
# models
from .models import Colors
# Serializers
from .serializers import ColorSerializer

"""
    CRUD with a viewset, don't forget to create the router.py 
    for using the viewset, this is for havingmor order in the project
"""
class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    # Override params
    queryset = Colors.objects.all()


