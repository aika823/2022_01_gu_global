from tkinter import CASCADE
from django.db import models


class Notice(models.Model):
    order = models.PositiveIntegerField(db_column="order", null=False, default=1)
    title = models.CharField(db_column="title", null=False, max_length=50)
    content = models.CharField(db_column="content", null=False, max_length=500)
    created_at = models.DateTimeField(db_column="created_at", null=False, auto_now_add=True)
    author = models.CharField(db_column="author", null=False,max_length=20)
    views = models.PositiveIntegerField(db_column="views", null=False, default=0)

    class Meta:
        db_table = "notice"