from django.contrib import admin
from .models import User,Post,Follow,Like

# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display=("username,"password")
# admin.site.register(User,UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=("user","content","timestamp")
admin.site.register(Post,PostAdmin)

class FollowAdmin(admin.ModelAdmin):
    list_display=("follower","followed")
admin.site.register(Follow,FollowAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display=("user","post")
admin.site.register(Like,LikeAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display=("username","password")
admin.site.register(User,UserAdmin)