from django.shortcuts import render
from django.views import generic

from .models import Post


def index(request):
    return render(request, 'Django/index.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'Django/BlogPage.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'Django/BlogPost.html'







