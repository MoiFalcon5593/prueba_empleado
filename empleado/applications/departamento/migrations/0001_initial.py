# Generated by Django 3.1.1 on 2020-09-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('shor_name', models.CharField(max_length=20, unique=True, verbose_name='Nombre corto')),
                ('anulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
            options={
                'verbose_name': 'Mi departamento',
                'verbose_name_plural': 'Areas de empresa',
                'ordering': ['name'],
                'unique_together': {('name', 'shor_name')},
            },
        ),
    ]
