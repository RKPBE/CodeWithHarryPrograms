#I have created this file for displaying name on wabe page it is a Second Program


from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>KAJAL</h1>  <a href = "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django code with Kajal</a>''')

def about(request):
    return HttpResponse("About KAJAL<a href='/'> back </a>")

def removepunc(request):
    return HttpResponse("removepunc KAJAL <a href='/'> back </a>")

def capitalizefirst(request):
    return HttpResponse("capitalizefirst KAJAL <a href='/'> back </a>")

def newlineremove(request):
    return HttpResponse("newlineremove KAJAL <a href='/'> back </a>")

def spaceremove(request):
    return HttpResponse("spaceremove KAJAL <a href='/'> back </a>")
