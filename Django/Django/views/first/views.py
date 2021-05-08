from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def THIS_IS_WHAT_WE_KNOW(request):
    a='<h4>Chainsmokers</h4>'
    return HttpResponse(a)
