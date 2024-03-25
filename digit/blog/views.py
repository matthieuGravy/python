
"""""
on peut aussi ajouter en 3e param le contexte
"""""
from django.shortcuts import render
from .mocks import Post

def index(request):
    posts = Post.all()
    return render(request, 'blog/index.html', {'posts': posts})

def show(request, id):
    post = Post.find(int(id))
    return render(request, 'blog/show.html', {'post': post})