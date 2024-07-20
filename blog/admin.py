from django.contrib import admin

from blog.models import Comment, Post, Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "avatar")


admin.site.register(Post)
admin.site.register(Comment)
