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
    ),
     path(
        'api/product/by-stok/',
        views.ListProductStok.as_view(),
        name='product-by-stok',
    ),
    path(
        'api/product/by-gender/<gender>',
        views.ListProductByGender.as_view(),
        name='product-by-gender',
    ),
    path(
        'api/product/filter/',
        views.ListProductsFilter.as_view(),
        name='product-filter',
    )
]

