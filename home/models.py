from django.db import models

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
    file = models.FileField(upload_to='portfolio_files/', blank=True, null=True)  # Add this field for downloadable files

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

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link order to the user
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when order was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when order was last updated
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Order status
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total price

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')  # Link to the order
    product = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE)  # The design product being purchased
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the item

    def get_total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.product.title} (Order #{self.order.id})"        

