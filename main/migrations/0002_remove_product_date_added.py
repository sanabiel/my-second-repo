# Generated by Django 4.2.4 on 2023-09-19 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
    ]
