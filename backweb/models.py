from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    keyword = models.CharField(max_length=20)
    tag = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
    desc = models.CharField(max_length=150)
    content = models.TextField()
    icon = models.ImageField(upload_to='article', null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'


class User(models.Model):
    truename = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    tel = models.CharField(max_length=11)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'

