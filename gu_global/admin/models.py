from django.db import models


class Admin(models.Model):
    
    username = models.CharField(db_column="username", null=False, max_length=20 ,default='')
    password = models.CharField(db_column="password", null=False, max_length=200, default='')

    class Meta:
        db_table = "admin"
