from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from .models import Project


# Create your views here.
class PortfolioJavaScript(generic.ListView):
    model = Project
    queryset = Project.objects.filter(technology=0).order_by('-date_created')
    template_name = 'Django/PortfolioJavaScript.html'
    context_object_name = 'project_list'


class PortfolioDetail(generic.DetailView):
    model = Project
    template_name = 'Django/PortfolioDetail.html'

