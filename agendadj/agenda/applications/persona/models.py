#
from model_utils.models import TimeStampedModel
#
from django.db import models

#Modelo Hobie
class Hobie(TimeStampedModel):
        hobie = models.CharField(
            'Pasa tiempo', 
            max_length=40,
        )
        class Meta:
            verbose_name = 'Hobie'
            verbose_name_plural = 'Hobbies'
        def __str__(self):
            return self.hobie
        


#Modelo Persona
class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """
    # Relationship
    hobiies = models.ManyToManyField(Hobie, verbose_name=("Hobies de la persona"))

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )


    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name


#Modelo reunión
class Meeting(TimeStampedModel):
    # Realationship with Person Model
    person = models.ForeignKey(
        Person, 
        verbose_name=("Paricipantes"), 
        on_delete=models.CASCADE
    )

    date = models.DateField()
    hora =  models.TimeField()
    issue = models.CharField(
        ("Ausnto"), 
        max_length=50,
    )

    class Meta:
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meetings'
    
    def __str__(self):
        return self.issue
    