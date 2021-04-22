# Generated by Django 3.1.8 on 2021-04-21 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0015_auto_20210421_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('contact_number', models.CharField(max_length=15)),
                ('contact_number_2', models.CharField(max_length=15)),
                ('contact_number_3', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]