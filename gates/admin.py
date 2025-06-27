from django.contrib import admin
from .models import Gate, Order

@admin.register(Gate)
class GateAdmin(admin.ModelAdmin):
    list_display = ['name', 'material', 'dimensions', 'price', 'slug']
    list_filter = ['material']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'gate', 'weight_kg', 'total_price', 'advance_paid', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'gate__name']
    readonly_fields = ['created_at']
