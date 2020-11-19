# Generated by Django 3.1.2 on 2020-11-19 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='person',
            unique_together={('alias', 'country')},
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.CheckConstraint(check=models.Q(age__gte=18), name='age_restrict'),
        ),
    ]
