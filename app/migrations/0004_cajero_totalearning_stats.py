# Generated by Django 4.2.10 on 2024-04-03 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_producto_unidadmedidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='cajero',
            name='totalEarning',
            field=models.FloatField(default=0, max_length=11),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='stats',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sellsOneWeek', models.FloatField(max_length=11)),
                ('sellsTwoWeek', models.FloatField(max_length=11)),
                ('sellsThreeWeek', models.FloatField(max_length=11)),
                ('sellsFourWeek', models.FloatField(max_length=11)),
                ('bestCashierMonth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cajero')),
            ],
        ),
    ]
