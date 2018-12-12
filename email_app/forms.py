from django import forms

from .models import EmailAppModel

class EmailAppForm(forms.ModelForm):
    class Meta:
        model = EmailAppModel
        fields = ('first_name', 'last_name', 'email')


