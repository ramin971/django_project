from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from .models import Book
from django.db.models import Avg
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
    try:
        # challenge_text=switcher.get(month,"error")
        challenge_text=switcher[month]
        return render(request,'challenges/challenge.html',{
        'text':challenge_text,
        'month_name':month
        })
    except:
        raise Http404

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
    }
def book_list(request):
    books=Book.objects.all().order_by('-rating')
    total=books.count()
    average=books.aggregate(Avg('rating'))
    return render(request,'challenges/books.html',{
        'books': books,
        'total_number_of_books':total,
        'average':average
    })


def detail_book(request,slug):
    # book=Book.objects.get(pk=id)
    book=get_object_or_404(Book,slug=slug)
    return render(request,'challenges/book_detail.html',{
        'book':book
    })