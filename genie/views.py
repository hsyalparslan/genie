from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .models import TaskTwoGenie, TaskTwoCustomer
from . import forms
from .forms import CustomerForm
# Create your views here.

FORMS = [("GenieForm1", forms.GenieForm1),
         ("GenieForm2", forms.GenieForm2),
         ("GenieForm3", forms.GenieForm3)]

TEMPLATES = {"GenieForm1": "genie/form1.html",
             "GenieForm2": "genie/form2.html",
             "GenieForm3": "genie/form3.html"}

def activity_list(request):
	wishes = TaskTwoCustomer.objects.all()
	activities = TaskTwoGenie.objects.all()
	return render(request, 'genie/activity_list.html', {'activities': activities, 'wishes': wishes})

class GenieWizard(SessionWizardView):
	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]

	def activity_new(request):

		wishes = TaskTwoCustomer.objects.all()
		activities = TaskTwoGenie.objects.all()
		return render(request, 'genie/activity_edit.html' , {'activities': activities, 'wishes': wishes})
	
	def get_context_data(self, form, **kwargs):
		context = super(GenieWizard, self).get_context_data(form=form, **kwargs)
		wishess = TaskTwoCustomer.objects.all()
		if self.steps.current == 'GenieForm3':
			context.update({'wishess': wishess})
		return context

	def done(self, form_list, **kwargs):
		instance = TaskTwoGenie()
		for form in form_list:
			for field, value in form.cleaned_data.items():
				setattr(instance, field, value)
		instance.save()
		return HttpResponseRedirect('/activity/list/')

def wish_new(request):
	if request.method == "POST":
		form = CustomerForm(request.POST)

		if form.is_valid():
			customer = form.save(commit=False)
			customer.save()
			return redirect('activity_list')
	else:
		wishes = TaskTwoCustomer.objects.all()
		form = CustomerForm()
	return render(request, 'genie/wish_new.html', {'form': form, 'wishes': wishes})

def index(request):
	return render(request, 'genie/index.html')
