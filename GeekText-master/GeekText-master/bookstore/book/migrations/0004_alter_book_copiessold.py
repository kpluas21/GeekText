# Generated by Django 4.1.6 on 2023-02-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_copiessold_alter_book_author_alter_book_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copiesSold',
            field=models.PositiveSmallIntegerField(default='0', null=True),
        ),
    ]
