from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import PortfolioProject, Order, OrderItem, Inquiry, ProjectMessage, UserProfile

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'client')
    search_fields = ('title', 'description', 'category')
    list_filter = ('category', 'date')
    fields = ('title', 'description', 'image', 'category',
              'client', 'date', 'tools', 'file', 'price')

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
    list_display = ('name', 'email', 'subject', 'created_at', 'replied')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at', 'replied')
    readonly_fields = ('name', 'email', 'subject', 'message', 'design_file', 'created_at')
    fields = ('name', 'email', 'subject', 'message', 'design_file', 'created_at', 'reply', 'replied')

    # Overriding the save method to send reply email when reply is added
    def save_model(self, request, obj, form, change):
        if 'reply' in form.changed_data and obj.reply:
            obj.replied = True  # Mark inquiry as replied
            send_mail(
                subject=f"Response to your inquiry about {obj.subject}",
                message=obj.reply,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[obj.email],
                fail_silently=False,
            )
        super().save_model(request, obj, form, change)

@admin.register(ProjectMessage)
class ProjectMessageAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('project', 'name', 'email', 'message', 'created_at')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'city', 'country')
    search_fields = ('user__username', 'phone_number', 'city', 'country')

# Automatically create UserProfile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
