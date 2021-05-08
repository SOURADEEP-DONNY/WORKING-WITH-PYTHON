from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn2_django(request):
    return render(request,'f2.html')


def learn2_python(request):
    return render(request,'f4.html')
