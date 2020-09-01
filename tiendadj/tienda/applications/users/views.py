#Third party apps
from rest_framework.views import APIView
from firebase_admin import auth
#Django imports
from django.shortcuts import render
#Serializers
from .serializers import (
    LoginSocialSerializer,
)
# Models
from .models import (
    User,
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
        # Decoded token by tools fribenase (auth)
        decoded_token =auth.verify_id_token(token)
        # Collect all infromation when token is decoded
        email = decoded_token['email']
        name = decoded_token['name']
        avatar = decoded_token['picture']
        email_verified = decoded_token['email_verified']
        # Create a user in django app
        _user, created = User.objects.get_or_create(
            email=email, #find by email if exist
            defaults={ #Create if not with following data
                'full_name':name,
                'email':email,
                'is_active':True
            }
        )
        return None
