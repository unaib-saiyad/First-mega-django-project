from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    avtar = models.ImageField(upload_to='avtar/', default='default.png')
    full_name = models.CharField(max_length=200, default='')
    mobile = models.CharField(max_length=200, default='')
    Address = models.CharField(max_length=200, default='')
    tag = models.CharField(max_length=100, default='')

    def __str__(self):
        return "%s" % self.user


class UserUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    website = models.URLField(max_length=200, default='')
    github = models.URLField(max_length=200, default='')
    twitter = models.URLField(max_length=200, default='')
    instagram = models.URLField(max_length=200, default='')
    facebook = models.URLField(max_length=200, default='')

    def __str__(self):
        return "%s" % self.user


class UserWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    work_title_1 = models.CharField(max_length=200, default='')
    work_title_2 = models.CharField(max_length=200, default='')
    work_title_3 = models.CharField(max_length=200, default='')
    work_title_4 = models.CharField(max_length=200, default='')
    work_title_5 = models.CharField(max_length=200, default='')
    work_val_1 = models.IntegerField(default=0)
    work_val_2 = models.IntegerField(default=0)
    work_val_3 = models.IntegerField(default=0)
    work_val_4 = models.IntegerField(default=0)
    work_val_5 = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.user
