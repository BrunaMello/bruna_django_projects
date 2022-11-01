from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('homepage', views.index, name='index'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

