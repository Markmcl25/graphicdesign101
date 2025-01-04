from django import forms
from .models import Inquiry, Order
from .models import ProjectMessage

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'subject', 'message', 'design_file']

        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name', 'email', 'phone', 'address', 'city', 'postal_code',
            'country', 'payment_method', 'status'
        ]
        widgets = {
            'status': forms.HiddenInput(),  # Keep status hidden, default is 'pending'
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number (Optional)',
            'address': 'Shipping Address',
            'city': 'City',
            'postal_code': 'Postal Code',
            'country': 'Country',
            'payment_method': 'Choose Payment Method',
        }

class ProjectMessageForm(forms.ModelForm):
    class Meta:
        model = ProjectMessage
        fields = ['name', 'email', 'message']        