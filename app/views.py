from django.http import HttpResponse, response
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_protect


def index(request):
    return render(request, 'index.html')


@csrf_protect
def dataprocessing(request):
    return render(request, 'dataprocessing.html')
