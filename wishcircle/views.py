from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .models import Circle
from . import forms
# Create your views here.

FORMS = [("CircleForm1", forms.CircleForm1),
         ("CircleForm2", forms.CircleForm2),
         ("CircleForm3", forms.CircleForm3)]

TEMPLATES = {"CircleForm1": "circle/form1.html",
             "CircleForm2": "circle/form2.html",
             "CircleForm3": "circle/form3.html",}

def circle_list(request):
	activities = Circle.objects.all()
	return render(request, 'circle/circle_list.html', {'activities': activities})

class CircleWizard(SessionWizardView):
	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]

	def circle_new(request):

		activities = Circle.objects.all()
		return render(request, 'circle/circle_edit.html' , {'activities': activities})
	
	def get_context_data(self, form, **kwargs):
		context = super(CircleWizard, self).get_context_data(form=form, **kwargs)
		wishess = Circle.objects.all()
		if self.steps.current == 'CircleForm9':
			context.update({'wishess': wishess})		
		return context


	def done(self, form_list, **kwargs):
		instance = Circle()
		for form in form_list:
			for field, value in form.cleaned_data.items():
				setattr(instance, field, value)
		instance.save()
		return HttpResponseRedirect('')


def index(request):
	return render(request, '/genie/index.html')
