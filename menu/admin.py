from django.contrib import admin
from .models import Menu, MenuItems



@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(MenuItems)
class AdminMenuItems(admin.ModelAdmin):
    list_display = ["name", "slug" ,"parent", "menu"]
# Register your models here.
