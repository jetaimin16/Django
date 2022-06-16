from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog) # admin 사이트에 Blog 객체 등록
admin.site.register(Comment)