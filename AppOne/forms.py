from django import forms

class FormClass(forms.Form):
    Name=forms.CharField(max_length=128)
