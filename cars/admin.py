from django.contrib import admin
from cars import models


class BrandAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'name',
    list_filter = 'name',
    search_fields = 'name',
    list_display_links = 'name',


class CarAdmin(admin.ModelAdmin):
    list_display = 'model', 'brand', 'cost', 'value', 'model_year',
    ordering = 'model',
    list_filter = 'brand',
    search_fields = 'model', 'brand',
    list_display_links = 'model',


admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.Car, CarAdmin)
