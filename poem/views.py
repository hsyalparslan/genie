from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .models import Poem
from . import forms
# Create your views here.

FORMS = [("PoemForm1", forms.PoemForm1)]

TEMPLATES = {"PoemForm1": "poem/form1.html",}

def poem_list(request):
	activities = Poem.objects.all()
	return render(request, 'poem/poem_list.html', {'activities': activities})

class PoemWizard(SessionWizardView):
	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]

	def poem_new(request):

		activities = Poem.objects.all()
		return render(request, 'poem/poem_edit.html' , {'activities': activities})
	

	def done(self, form_list, **kwargs):
		instance = Poem()
		for form in form_list:
			for field, value in form.cleaned_data.items():
				setattr(instance, field, value)
		instance.save()
		return HttpResponseRedirect('/start')

