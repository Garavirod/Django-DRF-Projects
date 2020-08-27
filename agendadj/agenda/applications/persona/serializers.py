from rest_framework import serializers, pagination
#Models
from .models import (
    Person,
    Hobie,
    Meeting,
)


""" 
    Serializadores del modelo persona
"""

# Serializar con un modelo directamente
class PersonaSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Person
        fields = ('__all__')


# Serializar sin ningun modelo
class PersonaSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()


# Extended serializerModel
class ExtendedSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(default=False)
    class Meta:
        model = Person
        fields = ('__all__')

"""
    Serializadores del modelo Hobie
"""

class HobbieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobie
        fields = ('__all__')

class PersonaHobiesSerializer(serializers.ModelSerializer):
    #To serializar a collection ManyToMany in other serializer
    hobiies = HobbieSerializer(many=True)
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobiies',
            'created',
        )


"""
    Serializadores del modelo Meeting
"""

class MeetingSerializer(serializers.ModelSerializer):
    #Reuse a serializiser to sending in other serializer
    person = PersonaSerializer()
    class Meta:
        model = Meeting
        fields = (
            'id',
            'date',
            'hora',
            'person',
        )

# SERIALIZER METHOD FIELD
class MeetingSerializer2(serializers.ModelSerializer):
    #  It  creates a fields that uses data from fields that already exist, (derivated atribute)
    # The result of fecha_hora it will be the reult of processig any data else
    # Always put the new filrd on the object's tuple fields 
    fecha_hora = serializers.SerializerMethodField()
    class Meta:
        model = Meeting
        fields = (
            'id',
            'date',
            'hora',
            'issue',
            'person',
            'fecha_hora', #new derivated attribute
        )
    """
        Method tha returns the precess data
        @params obj is each register in de json
        Always is this structure
    """
    def get_fecha_hora(self,obj):
        return str(obj.date) + '-' + str(obj.hora)

"""
    SerializaerLink
"""

class MeetingSerializerLink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meeting
        fields = (
            'id',
            'date',
            'hora',
            'issue',
            'person', #FK
        )
        #Here goes the model atribute is is goig to be a link
        extra_kwargs = {
            'person': {
                'view_name' : 'persona_app:detail-person',
                'lookup_field' : 'pk' #Mediante qué tributo va  a cargar el regostro
            }
        }


class PersonPaginationSerializer(pagination.PageNumberPagination):
    page_size = 3
    max_page_size = 100 #maxinun numer of pages loads on memory