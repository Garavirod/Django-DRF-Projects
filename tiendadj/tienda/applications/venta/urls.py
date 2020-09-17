# Django
from django.urls import include, re_path, path

# Local

from . import views

app_name = "venta_app"

urlpatterns = [
    path(
        'api/venta/reporte/',
        views.SaleReportView.as_view(),
        name="venta-reporte",
    ),
    path(
        'api/venta/register-sale/',
        views.RegisterSaleView.as_view(),
        name="venta-register-sale",
    )
]
