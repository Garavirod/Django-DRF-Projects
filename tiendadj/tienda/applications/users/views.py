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
    GoogleLoginView is a view that uses the serializer 
    LoginSocialSerializer to recieve the token

    APIView is like a Formview that no is for read, 
    delete or update, 

"""
class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer
    #override
    def post(self,request):
        # this line serializes the data in the request
        serializer_data = self.serializer_class(data=request.data)
        """ 
            Validate the serialized data
            verify is data is correctly abot the serielizer's structure
        """
        serializer_data.is_Valid(raise_exception=True)
        # If data is valid then
        token =  serializer_data.data.get('token_id')
        return None
