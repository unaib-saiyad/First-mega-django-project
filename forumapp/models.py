import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=100, default="")
    tags = models.CharField(max_length=50, default="")
    languages = models.CharField(max_length=50, default="")
    body = models.CharField(max_length=1000, default="")
    image = models.ImageField(upload_to='forum/', default='')
    publish_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(default=timezone.now)
    id_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return "%s%s" % (self.user, self.id_number)
