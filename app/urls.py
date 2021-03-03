from django.urls import path
from . import views

name_app = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('dataprocessing', views.dataprocessing, name='dataprocessing'),
]
