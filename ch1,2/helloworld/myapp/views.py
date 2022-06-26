from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
    # request 요청시 index.html 찍어보내줌(rendering)