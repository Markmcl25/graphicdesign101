from django.contrib import admin
from .models import PortfolioProject, Order, OrderItem, Inquiry

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

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'design_file', 'created_at')
