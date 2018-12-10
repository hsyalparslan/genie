from django import forms
from .models import Poem

class PoemForm1(forms.Form):
	p_number = forms.CharField(max_length=10000, help_text ="Your number", label="Your number")
	p_1 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="Your answer", label="1-	Can you describe the mood which the persona would be in?")
	p_2 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="Your answer", label="2-	What seems to be the persona’s wish?")
	p_3 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="Your answer", label="3-	What is the tone of the poem?")
