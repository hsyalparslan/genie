from django.urls import path
from .views import PoemWizard
from . import forms
from . import views
from .views import FORMS
urlpatterns = [
	path('poem/new', PoemWizard.as_view(FORMS), name='poem_new'),
	path('poem/list', views.poem_list, name='poem_list'),
]