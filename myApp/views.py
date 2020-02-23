from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse(" Django on Docker on AWS from Kiran ")

def hello(request):
    return HttpResponse(" Hello From Kiran ")
