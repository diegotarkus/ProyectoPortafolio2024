# Generated by Django 5.0.4 on 2024-06-27 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupones', '0001_initial'),
        ('ordenes', '0002_alter_orden_descuento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='cupon',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='cupones.cupon', verbose_name='cupon'),
        ),
    ]
