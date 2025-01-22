from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),  # Root URL for the homepage
    path('home/', views.index, name='index'),  # Alias for homepage
    path('shopping-bag/', views.shopping_bag, name='shopping_bag'),  # Shopping bag page
    path('portfolio/<int:project_id>/', views.project_detail, name='project_detail'),  # Individual project page
    path('portfolio/', views.portfolio, name='portfolio'),  # Portfolio page
    path('accounts/', include('allauth.urls')),  # Authentication routes
    path('submit-inquiry/', views.submit_inquiry, name='submit_inquiry'),  # Inquiry submission
    path('checkout/', views.checkout, name='checkout'),  # Checkout page
    path('checkout-success/', views.checkout_success, name='checkout_success'),  # Checkout success page
    path('add-to-cart/<int:project_id>/', views.add_to_cart, name='add_to_cart'),  # Add to cart
    path('update_quantity/<int:project_id>/', views.update_quantity, name='update_quantity'),  # Update cart quantity
    path('remove-item/<int:project_id>/', views.remove_item, name='remove_item'),  # Remove item from cart
]

# Serve media and static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
