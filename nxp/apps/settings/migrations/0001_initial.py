# Generated by Django 3.1.2 on 2020-10-18 03:38

from django.db import migrations, models
import nxp.core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('text_before_service', 'text_before_service'), ('about_us_title', 'about_us_title'), ('about_us_description', 'about_us_description'), ('about_us_img', 'about_us_img'), ('our_portfolio_title', 'our_portfolio_title'), ('our_portfolio_description', 'our_portfolio_description'), ('price_title', 'price_title'), ('price_description', 'price_description'), ('blog_title', 'blog_title'), ('blog_desc', 'blog_desc'), ('map_title', 'map_title'), ('latitude', 'latitude'), ('longitude', 'longitude'), ('contact_us_text', 'contact_us_text'), ('contact_us_description', 'contact_us_description'), ('contact_us_description_2', 'contact_us_description_2'), ('address', 'address'), ('phone', 'phone'), ('email', 'email'), ('website', 'website')], max_length=254, unique=True)),
                ('text_value', models.CharField(blank=True, max_length=254, null=True)),
                ('img_value', models.ImageField(upload_to=nxp.core.utils.FilenameGenerator(prefix='settings'))),
            ],
        ),
    ]