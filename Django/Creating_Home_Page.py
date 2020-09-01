from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #return HttpResponse("Home")
    dict1={'name':'Souradeep','location':'Kolkata'}
    return render(request,"index.html",dict1)
def removepunc(request):
    # GET THE TEXT
    djtext=request.GET.get('text','default')
    print(djtext)
    # ANALYSE THE TEXT
    return HttpResponse("removepunc <a href='/'>Back</a>")
def capfirst(request):
    return HttpResponse("Capitalize First <a href='/'>Back</a>")
def newlineremove(request):
    return HttpResponse("Newline remover <a href='/'>Back</a>")
