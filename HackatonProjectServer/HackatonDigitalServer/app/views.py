"""
Definition of views.
"""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from datetime import datetime
import urllib2
from app.serializers import LoginSerializer, UserSerializer
import io
import app.models


def getStatus(request):
    html = "<html><body>I'm the server, and i'm alright</body></html>"
    return HttpResponse(html)

@csrf_exempt
def login(request):
    try:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = LoginSerializer(data = data)
            if(serializer.is_valid()):
                logged_user = app.models.user.objects.get(username = data['username'],password = data['password'])
                serializer = UserSerializer(logged_user)
                return HttpResponse(serializer.data,status=202)
    except Exception as e:
        return HttpResponse(e,status=400)

@csrf_exempt
def setup_user(request):
    
    try:
        if request.method=='POST':
            data = JSONParser().parse(request)
            serializer = UserSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(serializer.data,status=201)
            else:
                return HttpResponse(serializer.errors,status=404)
    except Exception as e:
        return HttpResponse(e,status=400)