from django.shortcuts import render, redirect
# from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from . import forms
from . import models
# Create your views here.


@login_required(login_url="/login")
def Home(request):
    posts = models.Post.objects.all()

    # Delete by Author
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = models.Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request, 'home.html', {"posts": posts})


@login_required(login_url="login")
def create_post(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = forms.PostForm()

    return render(request, 'create_post.html', {"form": form})


@login_required(login_url="login")
def update_post(request, pk):

    # Update by Author
    post = models.Post.objects.get(id=pk)
    if request.method == "POST":
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.PostForm(instance=post)

    return render(request, 'update_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # messages.success(request, 'Account was created.')
            login(request, user)
            return redirect('home')
    else:
        form = forms.RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form})
