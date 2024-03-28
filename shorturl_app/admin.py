from django.contrib import admin
from .models import ShortUrl, Statistics
# Register your models here.

admin.site.register(Statistics)
admin.site.register(ShortUrl)

