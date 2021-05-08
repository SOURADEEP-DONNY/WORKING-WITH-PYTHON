from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app2_fun1(request):
    return HttpResponse('<h1>THIS IS FROM APP2 FUNCTION 1</h1>')
def app2_fun2(request):
    return HttpResponse('<h1>THIS IS FROM APP2 FUNCTION 2</h1>')
