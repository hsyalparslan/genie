from django import forms
from .models import TaskTwoCustomer

class GenieForm1(forms.Form):

	g_name = forms.CharField(max_length=100, help_text="e.g. Aladdin v2", label="")

class GenieForm2(forms.Form):
	honeypot = forms.CharField(required=False,
								widget=forms.HiddenInput,
								label="Leave empty",
							)

class GenieForm3(forms.Form):
	wishes = forms.ModelChoiceField(queryset=TaskTwoCustomer.objects.all(), label="Choose the wish of:", empty_label="Tap to choose")
	g_choice = forms.CharField(widget=forms.Textarea, label="Your justification:")


class CustomerForm(forms.ModelForm):

	class Meta:
		model = TaskTwoCustomer
		fields = ('c_name', 'c_wish',)
