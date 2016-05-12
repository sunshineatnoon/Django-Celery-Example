from django import forms
from .models import Calcu

class UserForm(forms.ModelForm):
    class Meta:
        model = Calcu
        fields = [
            "n",
        ]
