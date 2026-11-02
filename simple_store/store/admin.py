from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ("name_en", "category", "price", "stock", "is_featured")
  list_filter = ("category", "is_featured")
  search_fields = ("name_en", "name_hy", "name_ru")
  list_editable = ("price", "stock", "is_featured")
