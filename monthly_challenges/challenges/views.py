from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
# Create your views here.
switcher = {
    'january': 'it is work in january :)',
    'february': 'it is work in february :D',
    'march': 'it is work even in march !!',
    'april': 'it is work even in april !',
    'may': 'it is work even in may !!',
    'june': 'it is work even in june !',
    'july': 'it is work even in july !!',
    'august': 'it is work even in august !',
    'september': 'it is work even in september !!',
    'october': 'it is work even in october !',
    'november': 'it is work even in november !!',
    'december': None,
}
def monthly_challenge(request,month):
    challenge_text=switcher.get(month, 'error  :(')
    return render(request,'challenges/challenge.html',{
        'text':challenge_text,
        'month_name':month
    })

def monthly_challenge_by_number(request,month):
    months = list(switcher.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month-1]
    redirect_path = reverse('monthly_challenge_string',args=[redirect_month])

    return HttpResponseRedirect(redirect_path)
def home(request):
    months=list(switcher.keys())

    return render(request,'challenges/home.html',{
        'months':months
    })
