from django import forms
from .models import Car_Model, Brand_Model, Comments_Model


class BrandModel_Form(forms.ModelForm):
    class Meta:
        model = Brand_Model
        fields = '__all__'


class CarModel_Form(forms.ModelForm):
    class Meta:
        model = Car_Model
        fields = '__all__'


class CommentsModel_Form(forms.ModelForm):
    class Meta:
        model = Comments_Model
        fields = ['name', 'email', 'content']
