# Generated by Django 5.0.4 on 2024-04-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_factura_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cajero',
            name='password',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numeroCompras',
            field=models.IntegerField(),
        ),
    ]
