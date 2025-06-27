from django.contrib import admin
from .models import Gate, Order

@admin.register(Gate)
class GateAdmin(admin.ModelAdmin):
    list_display = ['name', 'material', 'dimensions', 'price', 'slug']
    list_filter = ['material', 'price']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['slug']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'gate', 'weight_kg', 'total_price', 'advance_paid', 'status', 'created_at', 'material']
    list_filter = ['status', 'created_at', 'gate__material']
    search_fields = ['user__username', 'gate__name']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    def material(self, obj):
        return obj.gate.material
    material.short_description = 'Material'
