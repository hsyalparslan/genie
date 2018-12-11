from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .models import Lamp
from . import forms
# Create your views here.

FORMS = [("LampForm1", forms.LampForm1),
         ("LampForm2", forms.LampForm2)]

TEMPLATES = {"LampForm1": "lamp/form1.html",
             "LampForm2": "lamp/form2.html",}

def lamp_list(request):
	activities = Lamp.objects.all()
	return render(request, 'lamp/lamp_list.html', {'activities': activities})

class LampWizard(SessionWizardView):
	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]

	def lamp_new(request):

		activities = Lamp.objects.all()
		return render(request, 'lamp/lamp_edit.html' , {'activities': activities})
	
	def get_context_data(self, form, **kwargs):
		context = super(LampWizard, self).get_context_data(form=form, **kwargs)
		wishess = Lamp.objects.all()
		if self.steps.current == 'LampForm9':
			context.update({'wishess': wishess})		
		return context


	def done(self, form_list, **kwargs):
		instance = Lamp()
		for form in form_list:
			for field, value in form.cleaned_data.items():
				setattr(instance, field, value)
		instance.save()
		return HttpResponseRedirect('/start')


def index(request):
	return render(request, 'genie/index.html')
