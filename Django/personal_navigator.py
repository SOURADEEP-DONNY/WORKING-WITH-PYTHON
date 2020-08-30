from django.http import HttpResponse

def home(request):
    return HttpResponse('''<h1>CREATED BY SOURADEEP</h1>
<a href="https://www.youtube.com/watch?v=HtMF973tXIY">
Django National Anthem</a>''')

##def home2(request):
##    return HttpResponse('''<h1>CREATED BY SOURADEEP</h1>
##<a1 href="https://www.youtube.com/watch?v=xwwAVRyNmgQ">
##Jai ho</a1>''')
