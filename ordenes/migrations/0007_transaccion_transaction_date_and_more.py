# Generated by Django 5.0.4 on 2024-07-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0006_alter_transaccion_card_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='transaction_date',
            field=models.CharField(null=True, verbose_name='fecha_trans'),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='accounting_date',
            field=models.CharField(max_length=4, verbose_name='fecha_auth'),
        ),
    ]
