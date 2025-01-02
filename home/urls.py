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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
