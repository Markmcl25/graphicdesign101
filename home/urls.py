from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', views.index, name='home'),  # Root URL for the homepage
    path('home/', views.index, name='index'),  # Allow "index" for backward compatibility
    path('shopping-bag/', views.shopping_bag, name='shopping_bag'),  # Shopping bag page
    path('portfolio/<int:project_id>/', views.project_detail, name='project_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),  # Portfolio page
    path('accounts/', include('allauth.urls')),  # Allauth routes for authentication
    path('submit-inquiry/', views.submit_inquiry, name='submit_inquiry'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout-success/', views.checkout_success, name='checkout_success'),
    path('add-to-cart/<int:project_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_quantity/<int:project_id>/', views.update_quantity, name='update_quantity'),
    path('remove-item/<int:project_id>/', views.remove_item, name='remove_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
