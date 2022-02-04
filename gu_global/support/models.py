from pyexpat import model
from tkinter import CASCADE
from django.db import models
from products.models import Product
from django.db.models.deletion import CASCADE


# 문의사항
class Contact(models.Model):
    order = models.PositiveIntegerField(db_column="order", null=False, default=1)
    title = models.CharField(db_column="title", null=False, max_length=50)
    content = models.CharField(db_column="content", null=False, max_length=500)
    created_at = models.DateTimeField(db_column="created_at", null=False, auto_now_add=True)
    author = models.CharField(db_column="author", null=False,max_length=20)
    views = models.PositiveIntegerField(db_column="views", null=False, default=0)

    class Meta:
        db_table = "contact"


# 공지사항
class Notice(models.Model):
    order = models.PositiveIntegerField(db_column="order", null=False, default=1)
    title = models.CharField(db_column="title", null=False, max_length=50)
    content = models.CharField(db_column="content", null=False, max_length=500)
    created_at = models.DateTimeField(db_column="created_at", null=False, auto_now_add=True)
    author = models.CharField(db_column="author", null=False,max_length=20)
    views = models.PositiveIntegerField(db_column="views", null=False, default=0)

    class Meta:
        db_table = "notice"


# 동영상
class Video(models.Model):
    order = models.PositiveIntegerField(db_column="order", null=False, default=1)
    title = models.CharField(db_column="title", null=False, max_length=50)
    sub_title = models.CharField(db_column="sub_title", null=False, max_length=50)
    content = models.CharField(db_column="content", null=False, max_length=500)
    created_at = models.DateTimeField(db_column="created_at", null=False, auto_now_add=True)
    link = models.CharField(db_column="link", null=False, max_length=500)

    class Meta:
        db_table = "video"


# 팝업
class Popup(models.Model):
    start = models.DateField(db_column="start", null=False)
    end = models.DateField(db_column="end", null=False)
    title = models.CharField(db_column="title", null=False, max_length=50)
    content = models.CharField(db_column="content", null=False, max_length=500)
    created_at = models.DateTimeField(db_column="created_at", null=False, auto_now_add=True)
    image = models.ImageField(upload_to="media/images/popup", db_column="image", null=True)

    class Meta:
        db_table = "popup"


# 다운로드
class Download(models.Model):
    product = models.ForeignKey(to=Product, db_column="product", on_delete=CASCADE)
    category = models.CharField(db_column="category", null=False, max_length=50)
    file = models.FileField(upload_to="media/download", db_column="file", null=False)

    class Meta:
        db_table = "download"
