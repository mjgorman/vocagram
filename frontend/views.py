from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """
    The main page, will end up being a timeline like page
    """
    name = "Jennifer"
    html = "<html><body> Hi %s. This is the index page.</body></html>" % name
    return HttpResponse(html)

