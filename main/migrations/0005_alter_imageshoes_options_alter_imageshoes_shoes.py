# Generated by Django 5.0.7 on 2024-08-06 23:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_shoes_image_imageshoes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageshoes',
            options={},
        ),
        migrations.AlterField(
            model_name='imageshoes',
            name='shoes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shoes'),
        ),
    ]
