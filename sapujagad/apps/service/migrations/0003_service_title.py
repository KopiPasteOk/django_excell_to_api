# Generated by Django 3.1.2 on 2020-10-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20201025_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]