#django
from django.urls import path

#local
from . import views
app_name = "users_app"

urlpatterns = [
    #Template login
    path(
        'login/',
        views.LoginUser.as_view(),
        name = "login",
    ),
    path(
        'api/google-login/',
        views.GoogleLoginView.as_view(),
        name = "users_login_google",
    )
]