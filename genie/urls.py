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
	path('wish/new/', views.wish_new, name='wish_new'),
	path('', views.index, name='index'),
	path('would/', views.would, name='would'),
	path('reading/', views.reading, name='reading'),
	path('start/', views.start, name='start'),
	path('etym/', views.etym, name='etym'),
]