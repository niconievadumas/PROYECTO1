# Generated by Django 4.0.5 on 2022-07-25 15:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0005_perro_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
