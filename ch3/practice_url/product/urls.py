from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist), # ./products/ 일 경우
    path('first/', views.productfirst),
]