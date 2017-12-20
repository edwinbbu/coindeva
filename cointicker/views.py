import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    url="https://koinex.in/api/ticker";
    r=requests.get(url)
    context={
        "data": r.json()
    }
    return render(request,"index.html",context);
