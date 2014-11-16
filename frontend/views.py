from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = "Jennifer"
    html = "<html><body> Hi %s. This is the index page.</body></html>" % name
    return HttpResponse(html)

