from django.http import JsonResponse
import json
from django.forms.models import model_to_dict

from products.models import Product
from products.serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response


def api_home_tradational(request):
    # collect request body
    body = request.body

    print(request.GET) # get your params
    data = {}
    try :
        data = json.loads(body)
    except :
        pass
    data['headers'] = dict(request.headers)  # enforce dictionary if you get JSONserialize error
    data['content_type'] = (request.content_type)
    print(data)
    return JsonResponse(data)


def api_models(request):
    data = Product.objects.all().first()
    resp = {}

    # #manual conversion -version 1
    # if data :
    #     resp['title'] = data.title
    #     resp['content'] = data.content
    #     resp['price'] = data.price

    #manual conversion -version 2
    if data :
        resp = model_to_dict(data)
    return JsonResponse(resp)


@api_view(["GET","POST"])
def api_view(request):
    instance = Product.objects.all()
    if instance :
        data = ProductSerializer(instance,many=True).data

    return Response(data) # rest_framework funcN`