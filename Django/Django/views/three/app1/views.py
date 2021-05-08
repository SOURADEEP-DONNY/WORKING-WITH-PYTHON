from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_django(request):
    return render(request,'f1.html')


def learn_python(request):
    return render(request,'f3.html')

def fromhttpresponse(request):
    return HttpResponse('FROM HTTPRESPONSE')

