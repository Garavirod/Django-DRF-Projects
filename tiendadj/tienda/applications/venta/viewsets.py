# third party apps
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
)
# serializer
from .serializers import (
    ProcessSaleSerializerV2,
    SaleReportSerializer,
)

# Models
from .models import (
    Sale,
    SaleDetail
)

# Foreign Models
from applications.producto.models import Product

# local
from django.utils import timezone


# It is not mandatory works with ModelViewSet
class ventaViewSet(viewsets.ViewSet):

    # Authetication verify
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        IsAuthenticated, #if is authenticated     
    ] 
    serializer_class = SaleReportSerializer
    queryset = Sale.objects.all()

    """
        You must define each viewset's function, beacasue of in this casse.        
    """

    def list(self,request,*args, **kwargs):
        queryset = Sale.objects.all()
        serializer = SaleReportSerializer(queryset,many=True)
        return Response(serializer.data)        

    # This method is activated by POST request by router viewSet
    def create(self,request):
        """ 
            deserializing data from http (POST)
            It is recived data in a json fromat and 'ProcessSaleSerializer' 
            deserialize that infromation,
            In brief, the frontend send infromation in a JSON fromat
        """ 
        _serialized_data = ProcessSaleSerializerV2(data=request.data)

        # Verify if data structue is correct
        _serialized_data.is_valid(raise_exception=True)

        # Access to data previosly validated
        # tipo_recibo = _serialized_data.validated_data['type_invoce']


        # This register a sale in BDD acordding to serializer structure
        _sale = Sale.objects.create(
            date_sale= timezone.now(),
            amount=0,
            count=0,
            type_invoce=_serialized_data.validated_data['type_invoce'], #validated_data is to acess th elem in the serializer such you defined
            type_payment=_serialized_data.validated_data['type_payment'],
            adreese_send=_serialized_data.validated_data['adreese_send'],
            user=self.request.user,
        )

        # Getting all products whose id's are in the array ['product]
        productos = Product.objects.filter(
            id__in= _serialized_data.validated_data['product']
        )

        # Getting the quantities
        quantities = _serialized_data.validated_data['quantities']
        

        # for each product in the sale wecreate a sale detail object
        sales_details = []
        _amount = 0
        _count = 0

        for producto, cantidad in zip(productos, quantities):
            
            # Obje type sale detail 
            sale_detail = SaleDetail(
                sale=_sale, # sale previously registered
                product=producto,
                count=cantidad,
                price_purchase=producto.price_purchase,
                price_sale=producto.price_sale
            )
            #Adding up the amount
            _amount += _amount + producto.price_sale*cantidad
            _count += _count + cantidad

            #Setting the total amount to Object Sale
            _sale.amount = _amount
            _sale.count = _count

            #Saving the data in Sale
            _sale.save()

            # Adding sale datil to list of sales detail
            sales_details.append(sale_detail)

        #Bulk create for save Sale detaisl of ech product
        SaleDetail.objects.bulk_create(sales_details)

        return Response({'success':'sale was registered successful'})

    def retrieve(self,request,pk=None):
        # Recover object
        sale = Sale.objects.get(id=pk)
        # Deserialize the object
        serializer = SaleReportSerializer(sale)
        # Retorn data
        return Response(serializer.data)
        