from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print_helloworld(request):
    return HttpResponse("hello world ");