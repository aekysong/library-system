# Generated by Django 2.0.13 on 2019-11-22 01:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writers', models.CharField(max_length=200)),
                ('book_status', models.BooleanField(default=True)),
                ('book_location', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
