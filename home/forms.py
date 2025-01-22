from django import forms
from .models import Inquiry, Order, ProjectMessage

class InquiryForm(forms.ModelForm):
    """Form for submitting inquiries about design services."""

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'subject', 'message', 'design_file']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'design_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class OrderForm(forms.ModelForm):
    """Form for placing an order with Stripe integration."""

    # Add stripe token field for payments
    stripe_token = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = [
            'name', 'email', 'phone', 'address', 'city', 'postal_code',
            'country', 'payment_method', 'status'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number (Optional)', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Shipping Address', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal Code', 'class': 'form-control'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.HiddenInput(),  # Keep status hidden, default to 'pending'
        }

        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address': 'Shipping Address',
            'city': 'City',
            'postal_code': 'Postal Code',
            'country': 'Country',
            'payment_method': 'Choose Payment Method',
        }


class ProjectMessageForm(forms.ModelForm):
    """Form for submitting messages related to a specific project."""

    class Meta:
        model = ProjectMessage
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 4, 'class': 'form-control'}),
        }
