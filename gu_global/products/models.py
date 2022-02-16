from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):
    main_category = models.CharField(db_column="main_category", max_length=50, null=True)
    order = models.PositiveIntegerField(db_column="order", null=False, default=1)
    name = models.CharField(db_column="name", max_length=50)
    detail = models.CharField(db_column="detail", max_length=200)
    class Meta:
        db_table = "category"


class Product(models.Model):
    name = models.CharField(db_column="order", null=False, max_length=50, default=1)
    title = models.CharField(db_column="title", null=False, max_length=50)
    sub_title = models.CharField(db_column="sub_title", null=False, max_length=50)
    content = models.CharField(db_column="content", null=False, max_length=500)

    category = models.ForeignKey(to=Category, db_column="category", on_delete=CASCADE)
    type = models.CharField(db_column="type", null=True, max_length=50)

    manual = models.FileField(upload_to="media/download", db_column="manual", null=True)
    brochure = models.FileField(upload_to="media/download", db_column="brochure", null=True)
    sheet = models.FileField(upload_to="media/download", db_column="sheet", null=True)

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