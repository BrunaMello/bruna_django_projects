from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from .models import Project


# Create your views here.
class PortfolioJavaScript(generic.ListView):
    model = Project
    queryset = Project.objects.filter(technology=0).order_by('-date_created')
    template_name = 'Django/PortfolioPage.html'
    context_object_name = 'project_list'


class PortfolioJava(generic.ListView):
    model = Project
    queryset = Project.objects.filter(technology=1).order_by('-date_created')
    template_name = 'Django/PortfolioPage.html'
    context_object_name = 'project_list'


class PortfolioPython(generic.ListView):
    model = Project
    queryset = Project.objects.filter(technology=2).order_by('-date_created')
    template_name = 'Django/PortfolioPage.html'
    context_object_name = 'project_list'


class PortfolioAndroid(generic.ListView):
    model = Project
    queryset = Project.objects.filter(technology=3).order_by('-date_created')
    template_name = 'Django/PortfolioPage.html'
    context_object_name = 'project_list'


class PortfolioApple(generic.ListView):
    model = Project
    queryset = Project.objects.filter(technology=4).order_by('-date_created')
    template_name = 'Django/PortfolioPage.html'
    context_object_name = 'project_list'


class PortfolioOther(generic.ListView):
    model = Project
    queryset = Project.objects.filter(technology=5).order_by('-date_created')
    template_name = 'Django/PortfolioPage.html'
    context_object_name = 'project_list'


class PortfolioDetail(generic.DetailView):
    model = Project
    template_name = 'Django/PortfolioDetail.html'
