# Generated by Django 3.1.2 on 2021-07-01 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serial_number', '0003_auto_20210628_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serialnumber',
            name='type',
            field=models.CharField(choices=[('U', 'U'), ('D', 'D')], default='U', max_length=10),
        ),
    ]