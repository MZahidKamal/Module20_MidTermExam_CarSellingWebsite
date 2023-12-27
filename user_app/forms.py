from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class UserSignup_ModelForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
        ]

class UserProfileEdit_ModelForm(UserChangeForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'id': 'required'}))
    password = None

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]
