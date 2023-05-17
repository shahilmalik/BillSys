# Generated by Django 2.0.7 on 2023-05-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20230501_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='pincode',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_pincode',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6),
        ),
    ]
