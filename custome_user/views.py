
from .models import CustomUser
from rest_framework import generics
from .models import CustomUser
from .serializer import CustomUserSerializer
from django.http import JsonResponse
import json 
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view



@api_view([ 'POST'])
def hello_world(request):
    data = request.data ;
    print("-----------------this is data ------------------------>")
    print(data);
    print("-----------------this is data ------------------------>")
    serialzer = CustomUserSerializer(data=request.data);
    if serialzer.is_valid():
        serialzer.save();
    print("not valid ");
    return JsonResponse(data= serialzer,safe=False);


 