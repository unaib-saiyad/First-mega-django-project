from django.db import models


# Create your models here.
class Query(models.Model):
    username = models.CharField(max_length=200, default='')
    fullname = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    mobile = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    state = models.CharField(max_length=100, default='')
    zip = models.CharField(max_length=100, default='')
    query = models.CharField(max_length=500, default='')

    def __str__(self):
        return "%s" % self.username
