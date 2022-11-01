from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('postportfolio/', views.postportfolio, name='postportfolio'),
    path('reactportfolio', views.reactportfolio, name='reactportfolio'),
    path('pythonportfolio', views.pythonportfolio, name='pythonportfolio'),
    path('androidportfolio', views.androidportfolio, name='androidportfolio'),
    path('appleportfolio', views.appleportfolio, name='appleportfolio'),
    path('javaportfolio', views.javaportfolio, name='javaportfolio'),
    path('othersportfolio', views.othersportfolio, name='othersportfolio'),

]
