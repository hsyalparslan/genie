from django.urls import path
from .views import GenieWizard
from .forms import GenieForm1
from .forms import GenieForm2
from .forms import GenieForm3
from . import views
from .views import FORMS
urlpatterns = [
	path('activity/new/', GenieWizard.as_view(FORMS), name='activity_new'),
	path('activity/list/', views.activity_list, name='activity_list'),
]