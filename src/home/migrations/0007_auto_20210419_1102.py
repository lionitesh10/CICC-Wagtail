# Generated by Django 3.1.8 on 2021-04-19 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_aboutpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='service_body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='service_subtitle',
            field=models.TextField(),
        ),
    ]
