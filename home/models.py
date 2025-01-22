from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_image = models.ImageField(

        upload_to='profile_images/',

        blank=True,

        null=True,

        default='profile_images/default-profile.jpg'

    )

    phone_number = models.CharField(max_length=15, blank=True, null=True)

    address = models.TextField(blank=True, null=True)

    city = models.CharField(max_length=100, blank=True, null=True)

    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):

        return self.user.username


class PortfolioProject(models.Model):
    CATEGORIES = [
        ('logo', 'Logo Design'),
        ('web', 'Web Design'),
        ('branding', 'Branding'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(

        upload_to='portfolio_images/',

        default='portfolio_images/default-image.jpg',  # Provide a default image

        blank=True,

        null=True

    )

    category = models.CharField(
        max_length=100, choices=CATEGORIES, blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    tools = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(
        upload_to='portfolio_files/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title

    def get_display_price(self):
        """Return formatted price for display."""
        return f"${self.price:.2f}"


class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)  # Track if the inquiry is replied
    reply_message = models.TextField(blank=True, null=True)  # Store admin's reply

    def __str__(self):
        return f"{self.subject} - {self.name}"


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

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    stripe_payment_intent = models.CharField(
        max_length=255, blank=True, null=True)
    stripe_charge_id = models.CharField(max_length=255, blank=True, null=True)
    paid = models.BooleanField(default=False)

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICES, default='credit_card')

    def __str__(self):
        return f"Order #{self.id} by {self.name} ({self.status})"

    def get_total_cost(self):
        """Calculate total cost of the order."""
        return sum(item.get_total_price() for item in self.items.all())

    def mark_as_paid(self, stripe_charge_id):
        """Mark order as paid and store Stripe charge ID."""
        self.paid = True
        self.status = 'completed'
        self.stripe_charge_id = stripe_charge_id
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total_price(self):
        """Calculate total price for the item."""
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.project.title} (Order #{self.order.id})"


class ProjectMessage(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)  # Track if the message is replied
    reply_message = models.TextField(blank=True, null=True)  # Store admin's reply

    def __str__(self):
        return f"Message from {self.name} for {self.project.title}"
