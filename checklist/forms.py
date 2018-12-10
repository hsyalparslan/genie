from django import forms
from .models import SmartPhone

class SmartPhoneForm(forms.ModelForm):
    class Meta:
        model = SmartPhone
        fields = ['smart_phone_ownership', 'smart_phone_ownership2', 'smart_phone_ownership3','smart_phone_ownership4','smart_phone_ownership5','smart_phone_ownership6','smart_phone_ownership7','smart_phone_ownership8','smart_phone_ownership9', 'smart_phone_usage']
        widgets = {
            'smart_phone_ownership': forms.RadioSelect,
            'smart_phone_ownership2': forms.RadioSelect,
            'smart_phone_ownership3': forms.RadioSelect,
            'smart_phone_ownership4': forms.RadioSelect,
            'smart_phone_ownership5': forms.RadioSelect,
            'smart_phone_ownership6': forms.RadioSelect,
            'smart_phone_ownership7': forms.RadioSelect,
            'smart_phone_ownership8': forms.RadioSelect,
            'smart_phone_ownership9': forms.RadioSelect,
            'smart_phone_usage': forms.Select,
        }