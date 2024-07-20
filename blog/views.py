from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    ProfileForm,
    PostForm,
    CommentForm,
)
from django.core.paginator import Paginator
import markdown2  # import markdown2
from django.urls import reverse


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            if User.objects.filter(username=username).exists():
                form.add_error("username", "Username already exists")
            elif User.objects.filter(email=email).exists():
                form.add_error("email", "Email already exists")
            else:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data["password"])
                user.save()
                Profile.objects.create(user=user)
                return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def profile_view(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user

    profile = get_object_or_404(Profile, user=user)
    return render(request, "profile.html", {"profile": profile})


@login_required
def edit_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile", username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, "edit_profile.html", {"form": form})


@login_required
def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form})


@login_required
def edit_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)
    return render(request, "edit_post.html", {"form": form})


@login_required
def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, "delete_post.html", {"post": post})


def home_view(request):
    # Fetch all posts and order by created_at
    posts = Post.objects.all().order_by("-created_at")

    # Convert markdown content to HTML with code formatting
    for post in posts:
        post.content_html = markdown2.markdown(
            post.content, extras=["fenced-code-blocks", "code-friendly"]
        )

    # Set up pagination
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Render the page with the paginated posts
    return render(request, "home.html", {"page_obj": page_obj})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.view_count += 1
    post.save()
    comments = post.comments.all()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect("post_detail", pk=post.pk)
        else:
            return redirect("login")
    else:
        form = CommentForm()

    # Convert markdown content to HTML with code formatting
    post.content_html = markdown2.markdown(
        post.content, extras=["fenced-code-blocks", "code-friendly"]
    )

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "post_detail.html", context)


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    post.save()
    return redirect("post_detail", pk=pk)


@login_required
def add_comment_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("home")
    else:
        form = CommentForm()
    return render(request, "add_comment.html", {"form": form})
