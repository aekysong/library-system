# Generated by Django 2.0.13 on 2019-11-22 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_system', '0002_remove_book_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowed_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Fav_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fav_list',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_system.Book'),
        ),
        migrations.AddField(
            model_name='fav_list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_system.Book'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='borrowed_book',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_system.Book'),
        ),
        migrations.AddField(
            model_name='borrowed_book',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
