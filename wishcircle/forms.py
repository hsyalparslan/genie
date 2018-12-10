from django import forms
from .models import Circle

class CircleForm1(forms.Form):
	c_number = forms.CharField(max_length=10000, help_text ="Your number", label="Your number")
	c_1 = forms.CharField(max_length=10000, help_text ="Your answer", label="The worm said, “I wish I were a/an ……….. then I would smell water up to three miles away and I would lift up to 770 pounds with my trunk. Additionally, there would not be a danger of being eaten accidentally.”")

	c_4 = forms.CharField(max_length=10000, help_text ="Your answer", label="The snake said, “I wish I were a/an ………… then I would identify a sound’s location much faster than a human would and I would have a sense of smell ranging from 100,000 to 1,000,000 times more sensitive than a human’s. Above all, the man would behave friendly towards me”.")


class CircleForm2(forms.Form):

	c_2 = forms.CharField(max_length=10000, help_text ="Your answer", label="The dog said, “I wish I were a/an ……. then I would dance to communicate important information, such as where a flower is or a new home I found, so language would give a chance to refer to different locations in that I would have property of displacement.”")
	c_3 = forms.CharField(max_length=10000, help_text ="Your answer", label="The duck said, “I wish I were a/an……. then I would swim along with dolphins and be descendants of mammals. Like all mammals, I would breathe air and I were warm-blooded. Most of all, I would be the biggest mammal in the World.”")


class CircleForm3(forms.Form):
	c_5 = forms.CharField(max_length=10000, help_text ="Your answer", label="The whale said, “I wish I were a/an …….. then I would live in trees, grasslands, mountains and forests and I would grab branches with both fingers and toes. I would use bodily movements to communicate and I would peel my fruit and I would eat my fruit not the skins.”")
	c_6 = forms.CharField(max_length=10000, help_text ="Your answer", label="The elephant said, “I wish I were a/an ……. then I would have long ears, short fluffy tails and limbs and thanks to them I would powerfully dig very fast. Additionally, I would have short legs and these legs help me to run very fast.”")