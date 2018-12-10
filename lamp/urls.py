from django.urls import path
from .views import LampWizard
from . import forms
from . import views
from .views import FORMS
urlpatterns = [
	path('lamp/new', LampWizard.as_view(FORMS), name='lamp_new'),
	path('lamp/list', views.lamp_list, name='lamp_list'),
]