from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LoginUser(TemplateView):
    #@overrride
    template_name = "users/login.html"

