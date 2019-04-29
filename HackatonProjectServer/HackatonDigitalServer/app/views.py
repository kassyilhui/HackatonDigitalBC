"""
Definition of views.
"""
from math import sin, cos, sqrt, atan2, radians
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from datetime import datetime
import urllib2
from app.serializers import LoginSerializer, UserSerializer
import io
import app.models
import json


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
                return HttpResponse(JSONRenderer().render(serializer.data),status=202)
    except Exception as e:
        return HttpResponse(e,status=400)

@csrf_exempt
def setup_user(request):
    try:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                inventory = app.models.inventory(user_id = app.models.user.objects.get(id=serializer["id"].value))
                inventory.save()
                return HttpResponse(JSONRenderer().render(serializer.data),status=201)
            else:
                return HttpResponse(serializer.errors,status=404)
    except Exception as e:
        return HttpResponse(e,status=400)

@csrf_exempt
def addProduct(request):
    try:
        if request.method == 'POST':
             data = JSONParser().parse(request)
             prod = product()
             prod.name = data['name']
             prod.description = data['description']
             prod.price = data['price']
             prod.save()

             user_ = user.objects.get(id=data['user_id'])
             inv_ = app.models.inventory.objects.get(user_id = user_)

             inv_pr = inventory_products()
             inv_pr.product_id = prod
             inv_pr.inventory_id = inv_
             inv_pr.quantity = data['quantity']
             inv_pr.save()
             return HttpResponse(status=202)

    except Exception as e:
        return HttpResponse(e,status=400)

@csrf_exempt
def search_product(request):
    try:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            lat1 = radians(data['current_lat'])
            lon1 = radians(data['current_lon'])
            search = data['description']
            price_min = data['price_min']
            price_max = data['price_max']
            range = data['range']
            print(search)
            product_list = app.models.product.objects.all()
            if not not search:
                #product_list=product_list.filter(description =str(search))

                print(product_list)
                print("1")
            if price_min > 0:
                product_list = product_list.filter(price__gte = price_min)

            if price_max > 0:
                product_list = product_list.filter(price__lte =price_max)

            inventory_products_ = []
            ranged_products = []
            ranged_products_ = []

            json_ = "[{}]"
            print("querycompletp")
            for product in product_list:
                print("for")
                if range > 0:
                    print("rango")
                    ranged_products_.append(searchedProduct(product.price,
                    product.description,
                    app.models.inventory_products.objects.get(product_id = product).inventory_id.user_id_id,
                    product.id,
                    distanceTo(lat1,lon1,
                               app.models.inventory_products.objects.get(product_id = product.id).inventory_id.user_id.pos_lat,
                               app.models.inventory_products.objects.get(product_id = product.id).inventory_id.user_id.pos_lon)))
                    for x in ranged_products_:
                        if range <= x.range:
                            ranged_products.insert(x)
                    json_ = json.dumps([ob.__dict__ for ob in ranged_products])
                else:
                    print("else")
                    p = searchedProduct()
                    p.description = product.description
                    p.price = product.price
                    p.user_id = app.models.inventory_products.objects.get(product_id = product.id).inventory_id.user_id_id
                    p.product_id = product.id
                    inventory_products_.append(p)
                    print("dumps")
                    json_ = json.dumps([ob.__dict__ for ob in inventory_products_])
            return HttpResponse(json_,status=201)
    except Exception as e:
        return HttpResponse(e,status=400)


def distanceTo(lat1, lon1,lat2,lon2):
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = (R * c) * 1000 #METERS
    return distance

class searchedProduct:
    range = 0.0
    price = 0.0
    description = ""
    user_id = 0
    product_id = 0