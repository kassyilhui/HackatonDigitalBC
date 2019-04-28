"""
Definition of views.
"""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from datetime import datetime
import urllib2

def getStatus(request):
    html = "<html><body>I'm the server, and i'm alright</body></html>"
    return HttpResponse(html)