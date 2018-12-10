from django.urls import path
from .views import FillWizard
from . import forms
from . import views
from .views import FORMS
urlpatterns = [
	path('fill/new', FillWizard.as_view(FORMS), name='fill_new'),
	path('fill/list', views.fill_list, name='fill_list'),
]