from django.contrib import admin

from .models import Advert, Category, City


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "city",
        "category",
        "views",
    )
    search_fields = (
        "title",
        "city__name",
        "category__name",
    )
    list_filter = (
        "city",
        "category",
        "views",
    )
    readonly_fields = ("views",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    fields = ("name",)
    list_display = (
        "id",
        "name",
    )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    fields = ("name",)
    list_display = (
        "id",
        "name",
    )
