# Generated by Django 2.0.7 on 2023-05-01 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=20)),
                ('company_gst', models.CharField(blank=True, max_length=16)),
                ('company_address_line1', models.CharField(blank=True, max_length=20)),
                ('company_address_line2', models.CharField(blank=True, max_length=20)),
                ('company_city', models.CharField(blank=True, max_length=20)),
                ('company_state', models.CharField(blank=True, max_length=15)),
                ('company_pincode', models.IntegerField(blank=True, max_length=6)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='pincode',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
    ]
