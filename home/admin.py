from django.contrib import admin
from .models import PortfolioProject

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'client')
    search_fields = ('title', 'description', 'category')
    list_filter = ('category', 'date')
    fields = ('title', 'description', 'image', 'category', 'client', 'date', 'tools', 'file')
