from django.shortcuts import render
from django.views.generic import ListView
#Django Rest Framework packages
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

# Importing models
from .models import (
    Person,
    Hobie,
    Meeting,
)

#Importing serializer
from .serializers import (
    PersonaSerializer,
    PersonaSerializer2,
    ExtendedSerializer,
    HobbieSerializer,
    MeetingSerializer,
    PersonaHobiesSerializer,
    MeetingSerializer2,
    MeetingSerializerLink
)

"""
    Parsear un elemento o instancia a otro de tipo Json y viceversa 
    se llama Serializar
"""

# Vista genérica simple basada en clases
class PersonaListView(ListView):
    template_name = "persona/personas.html"
    context_object_name = 'personas' #Diccionaro de contexto que se pasa a un template html
    def get_queryset(self):
        return Person.objects.all()

"""
    Peticiones HTTP para la API
"""

# GET

class PersonaListApiView(ListAPIView):
    serializer_class = PersonaSerializer #Este serializador trabja la infromación
    def get_queryset(self):
        return Person.objects.all()

class GetNames(ListAPIView):
    serializer_class = PersonaSerializer
    def get_queryset(self):
        extract = self.kwargs['namePersona']
        return Person.objects.filter(
            full_name__icontains = extract
        )

class GetOnePerson(RetrieveAPIView):
    serializer_class = PersonaSerializer
    #El query_Set es quien se encarga de manejar el modeo en cuestion
    queryset = Person.objects.filter()


class GetListPerson(ListAPIView):
    #@override
    serializer_class = PersonaSerializer2
    queryset = Person.objects.all()

class GetLitsPersonExtended(ListAPIView):
    serializer_class = ExtendedSerializer
    queryset = Person.objects.all()

class GetHobbies(ListAPIView):
    #@override
    serializer_class = HobbieSerializer
    queryset = Hobie.objects.all()
class GetMeetings(ListAPIView):
    #@override
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()

class GetPersonHobbies(ListAPIView):
    serializer_class = PersonaHobiesSerializer
    queryset = Person.objects.all()

class GetMeetings2(ListAPIView):
    serializer_class = MeetingSerializer2
    queryset = Meeting.objects.all()

class GetApiListaLink(ListAPIView):
    serializer_class = MeetingSerializerLink
    queryset = Meeting.objects.all()

# POST
class PersonCreateView(CreateAPIView):
    serializer_class = PersonaSerializer    
    
# DELTE

class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonaSerializer
    queryset = Person.objects.all()

# PUT

class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonaSerializer
    queryset = Person.objects.all()

class PersonRetrieveView(RetrieveUpdateAPIView):
    serializer_class = PersonaSerializer
    queryset = Person.objects.all()