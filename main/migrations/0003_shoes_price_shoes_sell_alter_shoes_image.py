# Generated by Django 5.0.7 on 2024-08-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_shoes_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='sell',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='image',
            field=models.ImageField(blank=True, upload_to='Images', verbose_name='Изображение'),
        ),
    ]
