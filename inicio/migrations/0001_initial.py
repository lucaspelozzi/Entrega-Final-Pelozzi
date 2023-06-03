from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('sub_titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField(max_length=100)),
                ('autor', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
    ]
