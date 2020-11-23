from django.db import models

# Create your models here.
class Person(models.Model):

    full_name=models.CharField("Name", max_length=50)
    country=models.CharField("Country", max_length=30)
    passport= models.CharField("Passport", max_length=50)
    age= models.IntegerField()
    alias=models.CharField("Alias", max_length=10)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        db_table="PersonModel" #Table will be named this way
        """Do not register anything where alias and country be the same """
        unique_together = ['alias','country']
        """ Using constrainst
            Do not register any user whose age was lower than 18
        """
        constraints=[
            models.CheckConstraint(check=models.Q(age__gte=18), name="age_restrict")
        ]

        """ 
            To avoid create a Model in BDD which 'Model' can be just
            like a reference that can be used in herence.
            we use abstract=true,so do not register in Admin.  
        """
        abstract = True

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse("Person_detail", kwargs={"pk": self.pk})

class Employee(Person):
    position=models.CharField('Position', max_length=50)
