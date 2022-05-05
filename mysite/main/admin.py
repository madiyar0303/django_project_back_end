from django.contrib import admin
from main.models import Post
from main.models import Comment


admin.site.register(Post)
admin.site.register(Comment)