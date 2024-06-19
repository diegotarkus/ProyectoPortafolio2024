# Generated by Django 5.0.4 on 2024-06-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='apellido')),
                ('correo', models.EmailField(max_length=254, verbose_name='correo')),
                ('mensaje', models.CharField(max_length=500, verbose_name='mensaje')),
                ('creado', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creado')),
            ],
        ),
    ]
