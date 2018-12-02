from django import forms
from fobi.base import BasePluginForm
from fobi.contrib.plugins.form_handlers.db_store import models
class SampleTextareaForm(forms.Form, BasePluginForm):

	plugin_data_fields = [
	("name", ""),
	("label", ""),
	("initial", ""),
	("required", False)
	]

	name = forms.CharField(label="Name", required=True)
	label = forms.CharField(label="Label", required=True)
	initial = forms.CharField(label="Initial", required=False)
	required = forms.BooleanField(label="Required", required=False)

