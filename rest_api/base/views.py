from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

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