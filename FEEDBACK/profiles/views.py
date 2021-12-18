from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic import CreateView,ListView
# Create your views here.

class ProfilesView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profile.html'
    context_object_name = 'profiles'
# 1
# def all_profile(request):
#     profiles=UserProfile.objects.all()
#     return render(request,'profiles/user_profile.html',{'profiles':profiles})


# def store_file(file):
#     with open("temp/image.jpg","wb+")as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    # form_class = ProfileForm
    success_url = '/profiles'


# class CreateProfileView(View):
#     def get(self,request):
#         form=ProfileForm()
#         return render(request,'profiles/create_profile.html',{'form':form})
#
#     def post(self,request):
#         form=ProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             print(form)
#             print("######")
#             print(request.FILES)
#             print("######")
#             print(request.POST)
#             print(request.POST['user_name'])
#             user_profile=UserProfile(image=request.FILES['user_image'])
#             user_profile.save()
#             # store_file(request.FILES['user_image'])
#             return HttpResponseRedirect("/profiles")
#         return render(request,'profiles/create_profile.html',{'form':form})
