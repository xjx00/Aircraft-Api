from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def hello(request):
    resp = {'Status': 200, 'Message': 'Hello AirCraft Control Apis.'}
    return JsonResponse(resp, safe=False)

