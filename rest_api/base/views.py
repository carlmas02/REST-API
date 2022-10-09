from django.shortcuts import render
from django.http import JsonResponse
import json

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
