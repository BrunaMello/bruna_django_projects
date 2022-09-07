from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


def index(request):
    return render(request, 'Django/index.html')


def blog(request):
    return render(request, 'Django/BlogPage.html')


def post(request):
    return render(request, 'Django/BlogPost.html')







