from django.contrib import admin
from .models import Login, UserUrl, UserWork

# Register your models here.

admin.site.register(Login)
admin.site.register(UserUrl)
admin.site.register(UserWork)
