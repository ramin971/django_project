from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            print(cd)
            user=authenticate(request,username=cd.get('username'),password=cd.get('password'))
            if user is not None:
                if user.is_active:
                    login(request,user)
                    redirect=request.POST['next']
                    print('###########redirect:',redirect)
                    if redirect == '' or None:
                        redirect='/'

                    print(type(redirect),'################')
                    return HttpResponseRedirect(redirect)
                else:
                    return HttpResponse('disable account')
            else:
                return HttpResponse('invalid login')
    else:
        form=LoginForm()

    return render(request,'accounts/login.html' ,{
        'form':form
    })