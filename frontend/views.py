""" The views for the project go here"""
#from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import logging
from frontend.models import Post

def index(request):
    """
    The main page, will end up being a timeline like page
    """
    logging.info(request)
    name = "USER"
    timeline = Post.objects.all()
    template = get_template('index.html')
    html = template.render(Context({'timeline' : timeline, 'name' : name}))
    return HttpResponse(html)
