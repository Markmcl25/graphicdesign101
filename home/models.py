from django.db import models
from django.contrib.auth.models import User

class PortfolioProject(models.Model):
    CATEGORIES = [
        ('logo', 'Logo Design'),
        ('web', 'Web Design'),
        ('branding', 'Branding'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.CharField(max_length=100, choices=CATEGORIES, blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    tools = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='portfolio_files/', blank=True, null=True)

    def __str__(self):
        return self.title

class Inquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    design_file = models.FileField(upload_to='design_uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} - {self.subject}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='credit_card')

    def __str__(self):
        return f"Order #{self.id} by {self.name} ({self.status})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total_price(self):
        """Calculate total price for the item."""
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.project.title} (Order #{self.order.id})"
