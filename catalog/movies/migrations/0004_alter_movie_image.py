# Generated by Django 4.0.3 on 2022-06-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_category_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='movies', verbose_name='Film Afişi'),
        ),
    ]
