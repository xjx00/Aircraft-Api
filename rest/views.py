from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def hello(request):
    resp = {'Status': 200, 'Message': 'Hello AirCraft Control Apis.'}
    return HttpResponse(json.dumps(resp), content_type="application/json")

