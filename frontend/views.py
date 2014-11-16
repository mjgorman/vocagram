""" The views for the project go here"""
#from django.shortcuts import render
from django.http import HttpResponse
import logging

def index(request):
    """
    The main page, will end up being a timeline like page
    """
    logging.info(request)
    name = "USER"
    html = "<html><body> Hi %s. This is the index page.</body></html>" % name
    return HttpResponse(html)

