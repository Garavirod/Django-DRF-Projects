from rest_framework import serializers
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
    #Resue a serializiser to sending in other serializer
    person = PersonaSerializer()
    class Meta:
        model = Meeting
        fields = (
            'id',
            'date',
            'hora',
            'person',
        )