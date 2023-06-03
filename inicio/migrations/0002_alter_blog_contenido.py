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
