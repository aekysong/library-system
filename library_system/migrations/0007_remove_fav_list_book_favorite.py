# Generated by Django 2.0.13 on 2019-11-23 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_system', '0006_fav_list_book_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fav_list',
            name='book_favorite',
        ),
    ]
