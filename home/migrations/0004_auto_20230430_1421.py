# Generated by Django 2.0.7 on 2023-04-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230427_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='GST',
        ),
        migrations.AddField(
            model_name='client',
            name='gst',
            field=models.CharField(default=None, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='address_line1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='address_line2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
