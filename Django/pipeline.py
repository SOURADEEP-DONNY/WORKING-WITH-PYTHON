from django.http import HttpResponse
def index(request):
    return HttpResponse("Home")
def removepunc(request):
    return HttpResponse("removepunc <a href='/'>Back</a>")
def capfirst(request):
    return HttpResponse("Capitalize First <a href='/'>Back</a>")
def newlineremove(request):
    return HttpResponse("Newline remover <a href='/'>Back</a>")
