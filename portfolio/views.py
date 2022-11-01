from django.shortcuts import render
from django.views import generic

from portfolio.models import Project


# Create your views here.
def portfolio(request):
    return render(request, 'Django/PortfolioPage.html')


def postportfolio(request):
    return render(request, 'Django/PostPortfolio.html')


def reactportfolio(request):
    project = Project.objects.all()
    context = {'project': project}
    return render(request, 'Django/ReactPortfolio.html', context)


def pythonportfolio(request):
    return render(request, 'Django/PythonPortfolio.html')


def androidportfolio(request):
    return render(request, 'Django/AndroidPortfolio.html')


def appleportfolio(request):
    return render(request, 'Django/ApplePortfolio.html')


def javaportfolio(request):
    return render(request, 'Django/JavaPortfolio.html')


def othersportfolio(request):
    return render(request, 'Django/OthersPortfolio.html')


