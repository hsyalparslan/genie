from django.urls import path
from .views import CircleWizard
from . import forms
from . import views
from .views import FORMS
urlpatterns = [
	path('circle/new', CircleWizard.as_view(FORMS), name='circle_new'),
	path('circle/list', views.circle_list, name='circle_list'),
]