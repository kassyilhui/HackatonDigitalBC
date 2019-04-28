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

@csrf_exempt
def login(request):
    try:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            log_user = LoginSerializer(data = data)
            if(serializer.is_valid()):
                logged_user = UserWarning.objects.get(username = data['username'],password = data['password'])
                serializer = UserSearializer(logged_user)
                return HttpResponse(serializer.data,status=201)
    except Exception as e:
        return HttpResponse(e,status=404)

@csrf_exempt
def setup_user(request):
    try:
        if request.method=='POST':
            stream = io.BytesIO(json)
            data = JSONParser().parse(stream)
            serializer = UserSerializer(data=data)
            serializer.object.save()