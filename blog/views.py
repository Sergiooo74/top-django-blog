from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .forms import PostForm
from .models import Post

"""
FBV - Function based views
CBV - Class based views
"""
def root(request):
    return render(request, template_name='blog/index.html')


def index(request):
    return render(request, template_name='blog/index.html')


def about(request):
    context = {
        "name": "Dmitri",
        "lastname": "Gorin",
        "email": "d.gorin@yandex.ru",
        "title": "About"
    }
    return render(request, template_name='blog/about.html', context=context)

def add_post(request):
    if request.method == "GET":
        form = PostForm()
        context = {
            'form': form,
            'title': 'Post adding'
        }
        return render(request, template_name='blog/add_post.html', context=context)

    if request.method == "POST":
        form = PostForm(dta=request.POST)
        if form.is_valid():
            post = Post()
            post.author = form.cleaned_data['author']
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            post.save()

            return index(request)



def post_list(request):
    # get all objects of model Post
    posts = Post.objects.all()
    context = {
        'title': 'Posts',
        'posts': posts
    }
    return render(request, template_name='blog/posts.html', context=context)

def post_detail(request, pk):
    # getting object with PK
    post = get_object_or_404(Post, pk=pk)
    context = {
        'title': 'Post info',
        'post': post
    }
    return render(request, template_name='blog/post_detail.html', context=context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(data=request.POST, isinstance=post)
        if form.is_valid():
            form.save()
            return post_list(request)
    else:
        form = PostForm(isinstance=post)
        context = {
            'form': form,
            'title': "Edit post"
        }
    return render(request, template_name="blog/post_edit.html", context=context)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
