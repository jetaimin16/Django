from django.urls import path
from board import views

urlpatterns = [
    path('', views.board), # ./boards/ 일 경우
    path('first/', views.boardfirst), # ./boards/first/
]