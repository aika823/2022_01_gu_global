# Generated by Django 4.0.1 on 2022-02-16 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0010_alter_notice_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='product',
            field=models.CharField(db_column='product', max_length=50),
        ),
    ]
