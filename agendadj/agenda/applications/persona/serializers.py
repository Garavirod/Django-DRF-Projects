from rest_framework import serializers
from .models import Person
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields =(
            'id',
            'full_name',
            'job',
            'email',
        )