# Generated by Django 4.1.6 on 2023-02-17 15:07

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_copiessold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, default=book.models.default_genre, max_length=200),
        ),
    ]
