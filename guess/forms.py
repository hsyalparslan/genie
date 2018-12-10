from django import forms
from .models import Guess

class GuessForm1(forms.Form):
	c_number = forms.CharField(max_length=10000, help_text ="Your number", label="Your number")
	c_1 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="Your guess on context & the person's wish(es)", label="")
class GuessForm2(forms.Form):
	c_2 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="Your guess on context & the person's wish(es)", label="")
class GuessForm3(forms.Form):
	c_3 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="Your guess on context & the person's wish(es)", label="")
class GuessForm4(forms.Form):
	c_4 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="Your guess on context & the person's wish(es)", label="")
class GuessForm5(forms.Form):
	c_5 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="Your guess on context & the person's wish(es)", label="")
class GuessForm6(forms.Form):
	c_6 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="Your guess on context & the person's wish(es)", label="")
