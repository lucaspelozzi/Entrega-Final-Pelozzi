from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_avatar_pic_modelousers_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelousers',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
