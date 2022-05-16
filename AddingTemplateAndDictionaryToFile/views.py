#I have created this file for displaying name on wabe page it is a Second Program


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Kajal', 'place':'Mars'}
    return render(request, 'index.html', params)

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
