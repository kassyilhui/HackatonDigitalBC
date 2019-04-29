"""
Definition of views.
"""
from math import sin, cos, sqrt, atan2, radians
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from datetime import datetime
import urllib2
from app.serializers import LoginSerializer, UserSerializer, InventoryProductsSerializer, OrderProductsSerializer
import io
import app.models
import json
from django.core import serializers as s

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
def getOrders(request):
    try:
        if request.method == 'POST':
             data = JSONParser().parse(request)
             user_ = app.models.user.objects.get(id=data['user_id'])
             
             if data['type'] == "1":
                 orders = app.models.order.objects.filter(owner_user_id = user_)
                 po = app.models.order_products.objects.filter(order_id__in=orders)
             elif data['type'] == "2":
                 orders = app.models.order.objects.get(requester_user_id = user_)
                 po = app.models.order_products.objects.filter(order_id__in=orders)

             serializer = OrderProductsSerializer(list(po), many=True)
             return HttpResponse(JSONRenderer().render(serializer.data),status=202)
    except Exception as e:
        return HttpResponse(e,status=400)

@csrf_exempt
def getProducts(request):
    try:
        if request.method == 'POST':
             data = JSONParser().parse(request)
             user_ = app.models.user.objects.get(id=data['user_id'])
             inv_ = app.models.inventory.objects.get(user_id = user_)
             ins = app.models.inventory_products.objects.filter(inventory_id=inv_)
             serializer = InventoryProductsSerializer(list(ins), many=True)
             return HttpResponse(JSONRenderer().render(serializer.data),status=202)
        elif request.method == 'GET':
             ins = app.models.inventory_products.objects.all()
             serializer = InventoryProductsSerializer(list(ins), many=True)
             return HttpResponse(JSONRenderer().render(serializer.data),status=202)
    except Exception as e:
        return HttpResponse(e,status=400)

@csrf_exempt
def setOrder(request):
    try:
        if request.method == 'POST':
             data = JSONParser().parse(request)
             order = app.models.order()
             order.owner_user_id =app.models.user.objects.get(id=data['owner'])
             order.requester_user_id = app.models.user.objects.get(id=data['user'])
             order.status_id = 0
             order.save()
             return JsonResponse({'order_id': order.id},status=202)

    except Exception as e:
        return HttpResponse(e,status=400)

@csrf_exempt
def setOrderProducts(request):
    try:
        if request.method == 'POST':
             data = JSONParser().parse(request)
             for order_p in data['products']:
                 order_produ = app.models.order_products()
                 order_produ.product_id = app.models.product.objects.get(id=order_p['product_id'])
                 order_produ.order_id = app.models.order.objects.get(id=order_p['order_id'])
                 order_produ.quantity = order_p['quantity']
                 order_produ.save()
             return HttpResponse(status=202)

    except Exception as e:
        return HttpResponse(e,status=400)


@csrf_exempt
def addProduct(request):
    try:
        if request.method == 'POST':
             data = JSONParser().parse(request)
             prod = app.models.product()
             prod.name = data['name']
             prod.description = data['description']
             prod.price = data['price']
             prod.type_id = 0
             prod.save()

             user_ = app.models.user.objects.get(id=data['user_id'])
             inv_ = app.models.inventory.objects.get(user_id = user_)

             inv_pr = app.models.inventory_products()
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
                    p = searchedProduct()
                    p.description = product.description
                    p.price = product.price
                    p.user_id = app.models.inventory_products.objects.get(product_id = product.id).inventory_id.user_id_id
                    p.product_id = product.id
                    inventory_products_.append(p)
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