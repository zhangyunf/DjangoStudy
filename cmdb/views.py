from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
import time

def login(resquest):
    return render(resquest, "login.html")

def home(resquest):
    return HttpResponse("<h1>cmdb</h1>")