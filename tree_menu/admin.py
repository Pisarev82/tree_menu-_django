from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'order')
    list_filter = ('menu_name',)
    search_fields = ('name', 'menu_name')
    fields = ('name', 'menu_name', 'parent', 'order', 'named_url', 'url')

admin.site.register(MenuItem, MenuItemAdmin)