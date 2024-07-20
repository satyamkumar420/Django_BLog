# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/edit/", views.edit_profile_view, name="edit_profile"),
    path("profile/<str:username>/", views.profile_view, name="profile"),
    path("profile/", views.profile_view, name="profile"),
    path("post/new/", views.create_post_view, name="create_post"),
    path("post/edit/<int:pk>/", views.edit_post_view, name="edit_post"),
    path("post/delete/<int:pk>/", views.delete_post_view, name="delete_post"),
    path("post/<int:pk>/", views.post_detail_view, name="post_detail"),
    path("post/<int:pk>/like/", views.like_post, name="like_post"),
    path("post/<int:pk>/comment/", views.add_comment_view, name="add_comment"),
]
