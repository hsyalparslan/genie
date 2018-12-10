from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .models import SmartPhone
from . import forms
from .forms import SmartPhoneForm
# Create your views here.

def checklist_new(request):
	if request.method == "POST":
		form = SmartPhoneForm(request.POST)

		if form.is_valid():
			customer = form.save(commit=False)
			customer.save()
			return redirect('check_list')
	else:
		form = SmartPhoneForm()
	return render(request, 'checklist/form1.html', {'form': form})

def check_list(request):
	hello = SmartPhone.objects.filter(smart_phone_ownership="No")
	hello2 = SmartPhone.objects.filter(smart_phone_ownership2="No")
	hello3 = SmartPhone.objects.filter(smart_phone_ownership3="No")
	hello4 = SmartPhone.objects.filter(smart_phone_ownership4="No")
	hello5 = SmartPhone.objects.filter(smart_phone_ownership5="No")
	hello6 = SmartPhone.objects.filter(smart_phone_ownership6="No")
	hello7 = SmartPhone.objects.filter(smart_phone_ownership7="No")
	hello8 = SmartPhone.objects.filter(smart_phone_ownership8="No")
	hello9 = SmartPhone.objects.filter(smart_phone_ownership9="No")
	hello10 = SmartPhone.objects.filter(smart_phone_usage="Clueless")
	return render(request, 'checklist/check_list.html', {'hello': hello,'hello2': hello2,'hello3': hello3,'hello4': hello4,'hello5': hello5,'hello6': hello6,'hello7': hello7,'hello8': hello8,'hello9': hello9,'hello10': hello10,})
