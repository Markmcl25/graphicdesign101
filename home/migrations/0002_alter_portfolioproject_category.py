# Generated by Django 5.1.4 on 2025-01-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioproject',
            name='category',
            field=models.CharField(blank=True, choices=[('logo', 'Logo Design'), ('web', 'Web Design'), ('branding', 'Branding')], max_length=100, null=True),
        ),
    ]
