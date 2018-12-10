from django.urls import path
from .views import GuessWizard
from . import forms
from . import views
from .views import FORMS
urlpatterns = [
	path('guess/new', GuessWizard.as_view(FORMS), name='guess_new'),
	path('guess/list', views.guess_list, name='guess_list'),
]