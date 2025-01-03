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
