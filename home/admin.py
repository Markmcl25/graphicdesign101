from django.contrib import admin
from .models import PortfolioProject
from .models import Order, OrderItem

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'client')
    search_fields = ('title', 'description', 'category')
    list_filter = ('category', 'date')
    fields = ('title', 'description', 'image', 'category', 'client', 'date', 'tools', 'file')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at')
    list_filter = ('status',)
    inlines = [OrderItemInline]    
