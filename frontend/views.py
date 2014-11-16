""" The views for the project go here"""
#from django.shortcuts import render
from django.http import HttpResponse
import logging
from frontend.models import Post

def index(request):
    """
    The main page, will end up being a timeline like page
    """
    logging.info(request)
    name = "USER"
    html = "<html><body> Hi %s. This is the timeline." % name
    for post in Post.objects.all():
        html = html + "<p>&nbsp;<font size = \"4\">" + str(post) + "<p><font size = \"2\">" + ("&nbsp;")*5 + "Likes: " + str(post.likes) + " User: " + post.user + " Date: " + str(post.pub_date)
    html = html + "</body></html>"
    return HttpResponse(html)
