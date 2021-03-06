"""practice_url URL Configuration

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
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second),
    path('products/', include('product.urls')),
    path('boards/', include('board.urls')),
]

# 상품 관련
    # 127.0.0.1:8000/products/1
    # 127.0.0.1:8000/products/2
    # 127.0.0.1:8000/products/3
# 구매 후기 관련
    # 127.0.0.1:8000/boards/1
    # 127.0.0.1:8000/boards/2
    # 127.0.0.1:8000/boards/3