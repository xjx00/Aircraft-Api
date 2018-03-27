from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def hello(request):
    resp = {'Status': 200, 'Message': 'Hello AirCraft Control Apis v2.0'}
    return Response(resp)

