from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['weight_kg', 'payment_proof']
        widgets = {
            'weight_kg': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'Enter weight in Kg'}),
            'payment_proof': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        } 