from django.shortcuts import render
import requests
import json

my_id = "" # API key

def home(request):

    url = "" + my_id
    response = requests.get(url)
    resdata = response.text
    obj = json.loads(resdata)
    obj = obj['results'] # 영화 data

    return render(request, 'index.html', {'obj':obj})