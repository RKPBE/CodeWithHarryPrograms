#I have created this file for displaying name on wabe page it is a Second Program


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About KAJAL<a href='/'> back </a>")

def removepunc(request):
    #get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #Analyse the text
    return HttpResponse("removepunc KAJAL <a href='/'> back </a>")

def capitalizefirst(request):
    return HttpResponse("capitalizefirst KAJAL <a href='/'> back </a>")

def newlineremove(request):
    return HttpResponse("newlineremove KAJAL <a href='/'> back </a>")

def spaceremove(request):
    return HttpResponse("spaceremove KAJAL <a href='/'> back </a>")
