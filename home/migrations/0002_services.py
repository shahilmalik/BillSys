# Generated by Django 2.0.7 on 2023-04-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
            ],
        ),
    ]
