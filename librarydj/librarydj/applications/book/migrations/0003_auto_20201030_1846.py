# Generated by Django 3.1.2 on 2020-10-30 18:46

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20201027_0118'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('object_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
