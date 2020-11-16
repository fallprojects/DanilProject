from django.contrib import admin
from .models import *


class News_admin(admin.ModelAdmin):
    list_display = ('name','description')
admin.site.register(News,News_admin)

admin.site.register(Games)
admin.site.register(Tag)
admin.site.register(Teams)

