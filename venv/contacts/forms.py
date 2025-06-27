from django import forms
from .models import Contact

class SaveContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'contact_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_type': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('', '---select---'),
                ('Family', 'Family'),
                ('Friend', 'Friend')
            ])
        }