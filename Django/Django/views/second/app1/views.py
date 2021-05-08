from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_fun1(request):
    return HttpResponse('<h1>THIS IS FROM APP1 FUNC 1</h1>')
def app1_fun2(request):
    return HttpResponse('<h1>THIS IS FROM APP1 FUNC 2</h1>')
