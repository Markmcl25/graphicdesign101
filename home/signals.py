from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order
from .models import Inquiry

@receiver(post_save, sender=Order)
def send_order_confirmation(sender, instance, created, **kwargs):
    if created:
        # Generate a PDF invoice or process order-related logic here.
        send_mail(
            subject=f"Order Confirmation - #{instance.id}",
            message=f"Thank you for your purchase, {instance.name}! Your order #{instance.id} has been received.",
            from_email='info@graphicdesign101.com',
            recipient_list=[instance.email],
            fail_silently=False,
        )

@receiver(post_save, sender=Inquiry)
def notify_admin_on_inquiry(sender, instance, created, **kwargs):
    if created:
        print(f"New inquiry from {instance.name}: {instance.subject}")