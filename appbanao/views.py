from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models
from . import forms

# Create your views here.
def signup(request):
    form = forms.MyUserCreationForm
    if request.method == "POST":
        form = forms.MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'appbanao/signup.html', {'form': form})

def posts(request):
    posts = models.Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'appbanao/posts.html', {'posts': posts,})

def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(models.Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'appbanao/post_detail.html', {'post': post})

def user_blog(request, user_id):
    if request.user.is_authenticated and request.user.role == 'Doctor':
        posts_req = models.Post.objects.filter(author__exact=request.user.id)
        return render(request, 'appbanao/adminblog.html', {'posts': posts_req})
    return render(request, 'appbanao/adminblog.html')


def blog_add(request):
    form = forms.BlogForm
    if request.method == "POST":
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'appbanao/addblog.html', {'form': form})