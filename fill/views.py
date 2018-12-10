from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .models import Fill
from . import forms
# Create your views here.

FORMS = [("FillForm1", forms.FillForm1),
         ("FillForm2", forms.FillForm2)]

TEMPLATES = {"FillForm1": "fill/form1.html",
             "FillForm2": "fill/form2.html",}

def fill_list(request):
	activities = Fill.objects.all()
	return render(request, 'fill/fill_list.html', {'activities': activities})

class FillWizard(SessionWizardView):
	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]

	def fill_new(request):

		activities = Fill.objects.all()
		return render(request, 'fill/fill_edit.html' , {'activities': activities})
	
	def get_context_data(self, form, **kwargs):
		context = super(FillWizard, self).get_context_data(form=form, **kwargs)
		wishess = Fill.objects.all()
		if self.steps.current == 'FillForm9':
			context.update({'wishess': wishess})		
		return context


	def done(self, form_list, **kwargs):
		instance = Fill()
		for form in form_list:
			for field, value in form.cleaned_data.items():
				setattr(instance, field, value)
		instance.save()
		return HttpResponseRedirect('/fill/list/')


def index(request):
	return render(request, 'genie/index.html')
