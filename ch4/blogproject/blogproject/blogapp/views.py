from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

def home(request):
    # 모든 블로그 글을 띄우는 코드
    posts = Blog.objects.all()
    # posts = Blog.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts':posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == "POST"):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# django form을 이용해 입력값을 받는 함수
# GET 요청(입력을 받을 수 있는 html 가져오기)
# POST 요청(입력한 내용을 DB에 저장. form에서 입력한 내용을 처리)
# 둘 다 처리 가능
def formcreate(request):
    if request.method == "POST":
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid(): # form에 받은 입력값이 유효할 경우
            # 저장하기 위한 코드
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')

    else: # GET 요청
        # 입력 받는 html 가져오기
        form = BlogForm()
    return render(request, 'form_create.html', {'form': form})

def modelformcreate(request):
    if request.method == "POST" or request.method == "FILES":
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() # form 자동 생성
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form': form})

def detail(request, blog_id):
    # blog_id번째 블로그 글을 가져오는 코드
    blog_detail = get_object_or_404(Blog, pk=blog_id) # 특정 개체 하나를 가져올 때 사용하는 메소드

    comment_form = CommentForm()
    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request, POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) # commit=False 저장하지 않고 대기
        filled_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id) # 게시물로 이동