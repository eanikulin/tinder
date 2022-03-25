# Generated by Django 4.0.2 on 2022-03-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_user_latitude_user_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=16, default=0.0, max_digits=30, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=16, default=0.0, max_digits=30, null=True, verbose_name='Долгота'),
        ),
    ]