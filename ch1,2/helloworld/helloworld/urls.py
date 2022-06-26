"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/foo', myapp.views.count), # http://127.0.0.1:8000/foo GET 요청시 myapp의 views.py 파일에 있는 count 함수 실행
    path('', myapp.views.home, name = 'hello_world'), # name: url path 이름 지정
]

# 현재 django url: http://127.0.0.1:8000/
# 특정 요청 주소1: http://127.0.0.1:8000/foo
# 특정 요청 주소2: http://127.0.0.1:8000/abc/1

# 1. views.py 내부에 함수 생성 - html rendering
# 2. urls.py의 path 경로로 연결 -> views.py의 함수 실행 -> html으로 연결