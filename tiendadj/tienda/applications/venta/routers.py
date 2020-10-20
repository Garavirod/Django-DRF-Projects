# third party app
from rest_framework.routers import DefaultRouter
# viewsets
from . import viewsets

router = DefaultRouter() #This creates a router for conecting with the viewsets

# Registering a route

"""
    The router catches the request
    done based on http protocol, viewset is very useful
    beacosue involes all viewsets such as :

        LisApiView,
        DetailAPIView
        Createview,
        DeleteView.

    for DELETE, PUT OR DELETE
    colors-list/pk/
"""
router.register(r'sales', viewsets.ventaViewSet,basename='sales')

# Definfining urlpatterns
urlpatterns = router.urls