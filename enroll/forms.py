from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'from-control'}),
            'email': forms.EmailInput(attrs={'class': 'from-control'}),
            'password': forms.PasswordInput(attrs={'class': 'from-control'}),

        }