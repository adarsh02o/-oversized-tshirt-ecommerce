from django.contrib import admin
from .models import TShirt

@admin.register(TShirt)
class TShirtAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'is_oversized', 'created_at']
    list_filter = ['is_oversized', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
