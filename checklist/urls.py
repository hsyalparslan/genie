from django.urls import path
from . import forms
from . import views
urlpatterns = [
	path('checklist/new', views.checklist_new, name='checklist_new'),
	path('checklist/list', views.check_list, name='check_list'),
]