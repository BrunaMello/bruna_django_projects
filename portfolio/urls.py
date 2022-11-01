from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('javascriptportfolio/', views.PortfolioJavaScript.as_view(), name='JavaScriptPortfolio'),
    path('<slug:slug>/', views.PortfolioDetail.as_view(), name='portfolio_detail'),
]
