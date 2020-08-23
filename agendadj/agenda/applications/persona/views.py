from django.shortcuts import render
from django.views.generic import ListView
#Django Rest Framework
from rest_framework.generics import ListAPIView

# Importing models
from .models import Person

#Importing serializer
from .serializers import PersonaSerializer

class PersonaListView(ListView):
    template_name = "persona/personas.html"
    context_object_name = 'personas' #Diccionaro de contexto que se pasa a un template html
    def get_queryset(self):
        return Person.objects.all()

class PersonaListApiView(ListAPIView):
    """
        Parsear un elemento a otro de tipo Json y viceversa se llama Serializar
    """
    serializer_class = PersonaSerializer #Este serializador trabja la infromación
    def get_queryset(self):
        return Person.objects.all()

class GetOnePerson(ListAPIView):
    serializer_class = PersonaSerializer
    def get_queryset(self):
        id = int(self.kwargs['idPersona'])        
        return Person.objects.get(id__exact=id)

class GetNames(ListAPIView):
    serializer_class = PersonaSerializer
    def get_queryset(self):
        extract = self.kwargs['namePersona']
        return Person.objects.filter(
            full_name__icontains = extract
        )
    
         
    

