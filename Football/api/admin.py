from django.contrib import admin
from .models import *


class News_admin(admin.ModelAdmin):
    class Meta:
        model = News
        list_display = ['name','description']

admin.site.register(News_admin,News)
