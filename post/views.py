from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *


def home(request):
    post = Post.objects.all()
    return render(request, template_name='post/home.html', context={
        'posts': post
    })

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post':post})


