from django.contrib import admin
from .models import Order, Item, Sundry, Equipment, Jobsite

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'jobsite', 'date_needed')


@admin.register(Sundry)
class SundryAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity_available')


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    display = ("name")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'quantity_requested', 'order')


@admin.register(Jobsite)
class Jobsite(admin.ModelAdmin):
    display = ("name")

