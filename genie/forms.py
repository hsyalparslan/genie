from django import forms


class GenieForm1(forms.Form):

	g_name = forms.CharField(max_length=100, help_text="e.g. Aladdin v2")

class GenieForm2(forms.Form):
	honeypot = forms.CharField(required=False,
								widget=forms.HiddenInput,
								label="Leave empty",
							)

class GenieForm3(forms.Form):
	g_choice = forms.CharField(widget=forms.Textarea)

