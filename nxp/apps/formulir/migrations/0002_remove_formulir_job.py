# Generated by Django 3.1.2 on 2020-12-13 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulir', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulir',
            name='job',
        ),
    ]
