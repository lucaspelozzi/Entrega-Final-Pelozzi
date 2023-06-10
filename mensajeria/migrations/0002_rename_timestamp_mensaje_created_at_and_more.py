# Generated by Django 4.2 on 2023-06-09 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_recibidos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_enviados', to=settings.AUTH_USER_MODEL),
        ),
    ]