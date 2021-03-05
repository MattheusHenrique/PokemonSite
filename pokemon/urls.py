from django.urls import path
from . import views

name_app = "pokemon"

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search')
]
