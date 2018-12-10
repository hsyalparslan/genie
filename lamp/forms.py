from django import forms
from .models import Lamp

class LampForm1(forms.Form):
	q_number = forms.CharField(max_length=10000, help_text ="Your number", label="Your number")
	q_1 = forms.CharField(max_length=10000, help_text ="Your answer", label="1-	Do you think that Aladdin’s wish about being rich is a good or a bad thing?")
	q_2 = forms.CharField(max_length=10000, help_text ="Your answer", label="2-	If you were in that cave, would you collect those treasure without asking to their owner?")
	q_3 = forms.CharField(max_length=10000, help_text ="Your answer", label="3-	If you were Aladdin, which wishes you want from the genie?")
	q_4 = forms.CharField(max_length=10000, help_text ="Your answer", label="4-	How would you feel if were left by your uncle in that cave and what would you do?")
	q_5 = forms.CharField(max_length=10000, help_text ="Your answer", label="5-	If you were the genie, would you grant all the wishes of Aladdin?")
	q_6 = forms.CharField(max_length=10000, help_text ="Your answer", label="6-	Do you think evil people could use Aladdin to make bad wishes? ")
	q_7 = forms.CharField(max_length=10000, help_text ="Your answer", label="7-	What would happen if genie granted wishes of evil people?")
	q_8 = forms.CharField(max_length=10000, help_text ="Your answer", label="8-	What is your wish from Aladdin? ")

class LampForm2(forms.Form):

	q_9 = forms.CharField(max_length=10000, label="")
