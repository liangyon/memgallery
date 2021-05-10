from django.contrib import admin

# Register your models here.
from .models import MyUser, ImageModel

admin.site.register(MyUser)
admin.site.register(ImageModel)