# Generated by Django 4.0.1 on 2022-02-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0016_alter_download_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(db_column='image', null=True, upload_to='media/images/video'),
        ),
    ]
