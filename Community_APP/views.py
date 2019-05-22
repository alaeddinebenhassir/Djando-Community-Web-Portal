from django.contrib.auth import login, authenticate , logout
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import SignUpForm ,PostForm , search
from .models import Post

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def post_new(request):
    if request.method == 'POST' :
        
        form= PostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('home')
    else :
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'dashbord.html', {'posts': posts})

def search_view(request):
    form = search(request.POST)
    if form.is_valid():
        key = form.cleaned_data('word')
        posts = Post.objects.get(headline__icontains=key)
    return render(request, 'search.html', {'posts': posts})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('home')
   
    