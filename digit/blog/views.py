
"""""
on peut aussi ajouter en 3e param le contexte
"""""
from django.shortcuts import render, get_object_or_404
# from .mocks import Post
from .models import Post
from django.http import Http404

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def show(request, id):
    post = get_object_or_404(Post, id=id)
    #try:
    #      post = Post.objects.get(id=id)
    #except :
    #    raise Http404("Post does not exist")
    return render(request, 'blog/show.html', {'post': post})