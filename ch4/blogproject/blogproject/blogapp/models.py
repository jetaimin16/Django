from django.db import models

class Blog(models.Model):
    # 숨겨진 primary key - id
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True) # 현재 시간 추가

    def __str__(self):
        return self.title # admin site의 블로그 글 title이 제목으로 뜨도록 지정

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    # 외래키를 이용하여 게시물과 연결
    # on_delete=models.CASCADE: 게시물 삭제시 함께 삭제

    def __str__(self):
        return self.comment