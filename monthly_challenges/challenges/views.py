from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

def january(request):
    return HttpResponse('it is work in january')

def february(request):
    return HttpResponse('hi february')
def monthly_challenge(request,month):
    switcher={
        'january': 'it is work in january :)',
        'february': 'it is work in february :D',
        'march': 'it is work even in march !!',
    }
    return HttpResponse(switcher.get(month,HttpResponseNotFound('error  :(')))