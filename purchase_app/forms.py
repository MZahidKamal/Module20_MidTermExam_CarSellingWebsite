from django import forms
from .models import Purchase_Model


class PurchaseModel_Form(forms.ModelForm):
    class Meta:
        model = Purchase_Model
        # fields = '__all__'
        fields = [
            'quantity',
            'payment_type',
        ]
