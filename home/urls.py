from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', views.index, name='home'),  # Root URL for the homepage
    path('home/', views.index, name='index'),  # Allow "index" for backward compatibility
    path('shopping-bag/', views.shopping_bag, name='shopping_bag'),  # Shopping bag page
    path('portfolio/', views.portfolio, name='portfolio'),  # Portfolio page
    path('accounts/', include('allauth.urls')),  # Allauth routes for authentication
]
