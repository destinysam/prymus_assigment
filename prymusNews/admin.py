from django.contrib import admin
# Register your models here.
from .models import News,ViewOnNews

admin.site.register(News)
admin.site.register(ViewOnNews)