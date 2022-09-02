from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    dic_context = {'msnegrito': "Testando negrito"}
    return render(request, 'Django/index.html', dic_context)


