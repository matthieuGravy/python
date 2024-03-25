
"""""
on peut aussi ajouter en 3e param le contexte
"""""
from django.shortcuts import render
# from .mocks import Post
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/show.html', {'post': post})