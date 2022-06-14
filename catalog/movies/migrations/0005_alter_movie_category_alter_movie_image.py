# Generated by Django 4.0.3 on 2022-06-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('', 'AKSİYON'), ('', 'MACERA'), ('', 'BİLİM-KURGU'), ('', 'ANİMASYON'), ('', 'BİYOGRAFİ')], max_length=1),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.TextField(verbose_name='Film Afişi'),
        ),
    ]
