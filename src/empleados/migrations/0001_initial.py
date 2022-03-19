# Generated by Django 4.0.1 on 2022-03-12 23:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('fecha_registro', models.DateField(default=datetime.datetime.now)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('edad', models.PositiveIntegerField(default=0)),
                ('salario', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('estado', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto/%Y/%m/%d')),
                ('cvitae', models.FileField(blank=True, null=True, upload_to='cvitae/%Y/%m/%d')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
