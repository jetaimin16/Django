from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    # POST 요청시 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user) # 로그인
            return redirect('home')
        else:
            return render(request, 'login.html')

    # GET 요청시 login form을 담고 있는 login.html 띄우기
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')