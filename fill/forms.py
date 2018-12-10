from django import forms
from .models import Fill

class FillForm1(forms.Form):
	f_number = forms.CharField(max_length=10000, help_text ="Your number", label="Your number")
	f_1 = forms.CharField(max_length=10000, help_text ="Your answer", label="When I was younger I watched a movie about a drum player. And I was so impressed. Then, my family bought a drum to me. But, there is a problem. We live in a flat. So, when I want to practice, our neighbour are disturbed. So, I wish...")
	f_2 = forms.CharField(max_length=10000, help_text ="Your answer", label="John sold his sport car yesterday. And he kept all of his money in his wallet instead of putting it in the bank. Then, suddenly he lost his wallet. I wish John...")
	f_3 = forms.CharField(max_length=10000, help_text ="Your answer", label="After got my exam grade, I understand that the most important thing is to start studying a few weeks before the exams and not leave it until the exam day. So, I wish...")
	f_4 = forms.CharField(max_length=10000, help_text ="Your answer", label="In our school, we don’t have to wear school uniform. However, I’m bored to decide what to wear in every morning. Because of thinking it, I started to be late to school. I wish...")


class FillForm2(forms.Form):

	f_5 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="...I wish I had taken a different job.", label="")
	f_6 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="...I wish I had listened to my mother’s advice.", label="")
	f_7 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="...I wish I had not got married.", label="")
	f_8 = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), help_text ="...I wish I had saved more money when I was younger.", label="")