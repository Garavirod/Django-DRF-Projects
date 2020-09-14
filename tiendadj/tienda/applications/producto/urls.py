# Django
from django.urls import  include, re_path, path

# Local
from . import views

app_name = "producto_app"

urlpatterns = [
    # Products list by user
    path(
        'api/product/by-user/',
        views.ListProductByUserView.as_view(),
        name='product-by-user',
    )
]

