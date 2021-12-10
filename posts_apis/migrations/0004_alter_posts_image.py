# Generated by Django 4.0 on 2021-12-10 15:03

from django.db import migrations, models
import posts_apis.helpers.src.image_file


class Migration(migrations.Migration):

    dependencies = [
        ('posts_apis', '0003_alter_posts_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posts_apis.helpers.src.image_file.ImageManage.set_image_file),
        ),
    ]
