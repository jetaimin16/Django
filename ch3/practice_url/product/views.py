from django.shortcuts import render

def productlist(request):
    return render(request, 'board.html')

def productfirst(request):
    return render(request, 'boardfirst.html')