# Generated by Django 4.0.1 on 2022-01-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='author',
            field=models.CharField(db_column='author', max_length=20),
        ),
    ]
