from django.contrib import admin
from cars.models import Car, Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'name',
    list_filter = 'name',
    search_fields = 'name',
    list_display_links = 'name',


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = 'model', 'brand', 'cost', 'value', 'model_year',
    ordering = 'model',
    list_filter = 'brand',
    search_fields = 'model', 'brand',
    list_display_links = 'model',
