from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelousers',
            old_name='avatar',
            new_name='avatar',
        ),
    ]
