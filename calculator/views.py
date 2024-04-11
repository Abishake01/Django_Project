from django.shortcuts import render
from django.http import HttpResponse
def page(request):
    return HttpResponse('<h1>Home Page</h1> /calculator --> Calculator app , /voting --> voting App')
  