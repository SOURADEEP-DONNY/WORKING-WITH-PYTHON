from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index_analy.html')

def analyze(request):

    # GET THE TEXT
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    
    if removepunc =="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        dict1={'purpose':'Removed Punctuation','analyzed_text':analyzed}

        return render(request,'analy.html',dict1)

    else:
        return HttpResponse('ERROR')

