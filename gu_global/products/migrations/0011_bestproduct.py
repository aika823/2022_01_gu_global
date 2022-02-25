# Generated by Django 4.0.1 on 2022-02-25 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_column='order', default=1)),
                ('name', models.CharField(db_column='name', max_length=50)),
                ('image', models.ImageField(upload_to='media/images/best_product')),
            ],
            options={
                'db_table': 'best_product',
            },
        ),
    ]
