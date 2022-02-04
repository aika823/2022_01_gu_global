from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):
    name = models.CharField(db_column="name", max_length=50)
    detail = models.CharField(db_column="detail", max_length=200)
    class Meta:
        db_table = "category"


class Product(models.Model):
    category = models.ForeignKey(to=Category, db_column="category", on_delete=CASCADE)
    name = models.CharField(db_column="order", null=False, max_length=50, default=1)
    title = models.CharField(db_column="title", null=False, max_length=50)
    sub_title = models.CharField(db_column="sub_title", null=False, max_length=50)
    content = models.CharField(db_column="content", null=False, max_length=500)
    class Meta:
        db_table = "product"


class ProductImage(models.Model):
    product = models.ForeignKey(to=Product, db_column="product", on_delete=CASCADE)
    image = models.ImageField(upload_to=("media/images/product"))
    class Meta:
        db_table = "product_image"


class ProductDetailImage(models.Model):
    product = models.ForeignKey(to=Product, db_column="product", on_delete=CASCADE)
    image = models.ImageField(upload_to=("media/images/product_detail"))
    class Meta:
        db_table = "product_detail_image"