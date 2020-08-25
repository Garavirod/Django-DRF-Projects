# Generated by Django 3.0.5 on 2020-08-24 18:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('hobie', models.CharField(max_length=40, verbose_name='Pasa tiempo')),
            ],
            options={
                'verbose_name': 'Hobie',
                'verbose_name_plural': 'Hobbies',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', models.DateField()),
                ('hora', models.TimeField()),
                ('issue', models.CharField(max_length=50, verbose_name='Ausnto')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Person', verbose_name='Paricipantes')),
            ],
            options={
                'verbose_name': 'Meeting',
                'verbose_name_plural': 'Meetings',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='hobiies',
            field=models.ManyToManyField(to='persona.Hobie', verbose_name='Hobies de la persona'),
        ),
    ]