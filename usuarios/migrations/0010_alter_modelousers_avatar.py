# Generated by Django 4.2 on 2023-06-07 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_modelousers_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelousers',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares/'),
        ),
    ]
