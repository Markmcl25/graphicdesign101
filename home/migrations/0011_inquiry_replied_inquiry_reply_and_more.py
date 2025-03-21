# Generated by Django 5.1.4 on 2025-01-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='replied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='reply',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='design_file',
            field=models.FileField(blank=True, null=True, upload_to='inquiries/'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
