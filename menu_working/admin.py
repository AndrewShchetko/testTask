from django.contrib import admin
from .models import *


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'menu_name', 'order', 'depth')
    list_display_links = ('id', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Menu, MenuAdmin)
