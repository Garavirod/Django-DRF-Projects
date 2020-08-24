from rest_framework import serializers
from .models import Person


# Serializar con un modelo directamente
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields =(
        #     'id',
        #     'full_name',
        #     'job',
        #     'email',
        # )
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