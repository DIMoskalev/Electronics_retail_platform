from django.contrib import admin

from store.models import Link, Product


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "level", "country", "city", "debt", "supplier")
    list_filter = ("city", "country",)
    list_display_links = ("supplier",)
    actions = ('clear_debt',)

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product_model", "release_date", "supplier")
    list_filter = ("supplier", "release_date")
    search_fields = ("name", "supplier",)
