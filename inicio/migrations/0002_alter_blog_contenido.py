# Generated by Django 4.2 on 2023-05-30 18:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contenido',
            field=ckeditor.fields.RichTextField(max_length=100),
        ),
    ]
