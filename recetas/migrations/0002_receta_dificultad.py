# Generated by Django 4.1.7 on 2023-03-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='dificultad',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
