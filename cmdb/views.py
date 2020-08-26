from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
import time

def home(resquest):
    return HttpResponse("<h1>cmdb</h1>")