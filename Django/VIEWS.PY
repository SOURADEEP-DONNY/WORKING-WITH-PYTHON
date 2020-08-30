#CREATED BY SOURADEEP!!!
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Donny")
def end_point(request):
    return HttpResponse("Hey Donny nice job")
