# Generated by Django 2.0.13 on 2019-11-22 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
    ]
