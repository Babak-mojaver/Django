from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"blog/index.html")