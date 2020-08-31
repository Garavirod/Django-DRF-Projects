#Third app
from rest_framework.views import APIView
#Django imports
from django.shortcuts import render
#Serializers
from .serializers import (
    LoginSocialSerializer,
)

# Create your views here.
from django.views.generic import TemplateView


class LoginUser(TemplateView):
    #@overrride
    template_name = "users/login.html"

""" 
    GoogloginView is a view that uses the serializer 
    LoginSocialSerializer to recieve the token

    APIView is like a Formview that no is for read, 
    delete or update, 

"""
class GoogloginView(APIView):
    serializer_class = LoginSocialSerializer