# Generated by Django 4.1.6 on 2023-02-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='copiesSold',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveSmallIntegerField(default=1970),
            preserve_default=False,
        ),
    ]
