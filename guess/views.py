from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .models import Guess
from . import forms
# Create your views here.

FORMS = [("GuessForm1", forms.GuessForm1),
         ("GuessForm2", forms.GuessForm2),
         ("GuessForm3", forms.GuessForm3),
         ("GuessForm4", forms.GuessForm4),
         ("GuessForm5", forms.GuessForm5),
         ("GuessForm6", forms.GuessForm6)]

TEMPLATES = {"GuessForm1": "guess/form1.html",
             "GuessForm2": "guess/form2.html",
             "GuessForm3": "guess/form3.html",
             "GuessForm4": "guess/form4.html",
             "GuessForm5": "guess/form5.html",
             "GuessForm6": "guess/form6.html",}

def guess_list(request):
	activities = Guess.objects.all()
	return render(request, 'guess/guess_list.html', {'activities': activities})

class GuessWizard(SessionWizardView):
	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]

	def guess_new(request):

		activities = Guess.objects.all()
		return render(request, 'guess/guess_edit.html' , {'activities': activities})
	
	def get_context_data(self, form, **kwargs):
		context = super(GuessWizard, self).get_context_data(form=form, **kwargs)
		wishess = Guess.objects.all()
		if self.steps.current == 'GuessForm9':
			context.update({'wishess': wishess})		
		return context


	def done(self, form_list, **kwargs):
		instance = Guess()
		for form in form_list:
			for field, value in form.cleaned_data.items():
				setattr(instance, field, value)
		instance.save()
		return HttpResponseRedirect('')


def index(request):
	return render(request, '/genie/index.html')
