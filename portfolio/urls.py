from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('javascriptportfolio/', views.PortfolioJavaScript.as_view(), name='JavaScriptPortfolio'),
    path('javaportfolio/', views.PortfolioJava.as_view(), name='JavaPortfolio'),
    path('pythonportfolio/', views.PortfolioPython.as_view(), name='PythonPortfolio'),
    path('androidportfolio/', views.PortfolioAndroid.as_view(), name='AndroidPortfolio'),
    path('appleportfolio/', views.PortfolioApple.as_view(), name='ApplePortfolio'),
    path('otherportfolio/', views.PortfolioOther.as_view(), name='OtherPortfolio'),
    path('<slug:slug>/', views.PortfolioDetail.as_view(), name='portfolio_detail'),
]
