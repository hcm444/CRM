from django import forms
from .models import Customer, Note

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']