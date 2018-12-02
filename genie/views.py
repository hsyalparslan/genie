from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .models import Activity
from . import forms
# Create your views here.

FORMS = [("GenieForm1", forms.GenieForm1),
         ("GenieForm2", forms.GenieForm2),
         ("GenieForm3", forms.GenieForm3)]

TEMPLATES = {"GenieForm1": "genie/form1.html",
             "GenieForm2": "genie/form2.html",
             "GenieForm3": "genie/form3.html"}

def activity_list(request):

	activities = Activity.objects.all()
	return render(request, 'genie/activity_list.html', {'activities': activities})

class GenieWizard(SessionWizardView):
	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]

	def activity_new(request):
		return render(request, 'genie/activity_edit.html')

	def done(self, form_list, **kwargs):
		instance = Activity()
		for form in form_list:
			for field, value in form.cleaned_data.items():
				setattr(instance, field, value)
		instance.save()
		return HttpResponseRedirect('/activity/list/')

