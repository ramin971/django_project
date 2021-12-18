from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView
from .models import Review
# Create your views here.

class ReviewView(CreateView):
    template_name = "reviews/review.html"
    model = Review
    form_class = ReviewForm
    success_url = "/tank-you"

# 3
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#

# 2
# class ReviewView(View):
#     def get(self,request):
#         form=ReviewForm()
#         return render(request,'reviews/review.html',{'form':form})
#     def post(self,request):
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request,'reviews/review.html',{'form':form})
#


# 1
# def review(request):
#     if request.method=='POST':
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # review=Review(user_name=form.cleaned_data['user_name'],
#             #               review_text=form.cleaned_data['review_text'],
#             #               rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save()
#             return HttpResponseRedirect("thank-you")
#     # if request.method=='POST':
#     #     username=request.POST['username']
#     #     print(username)
#     #     return HttpResponseRedirect('thank-you')
#     else:
#         form=ReviewForm()
#     return render(request,"reviews/review.html",{
#         'form':form
#     })
# class Home(ListView):
#     template_name = "reviews/home.html"
#     model = Review
#     # context_object_name = "all_data"
#     def get_context_data(self, *, object_list=None, **kwargs):
#         contex=super().get_context_data(**kwargs)
#         fav_id=self.request.session.get("favorite_review")
#         contex["fav_obj"]=self.request.objects.get(pk=fav_id)
#         return contex
    # def get(self, request, *args, **kwargs):
    #     fav_obj = self.request.session.get("favorite_review",0)
    #     print(fav_obj)
    #     return super().get(request,*args,**kwargs)



    # def get_queryset(self):
    #     base_data=super().get_queryset()
    #     data=base_data.filter(rating__gt=3)
    #     return data

# 2
# class Home(TemplateView):
#     template_name = "reviews/home.html"
#     def get_context_data(self, **kwargs):
#         contex=super().get_context_data(**kwargs)
#         all_data=Review.objects.all()
#         contex["all_data"]=all_data
#         return contex

# 1
def home(request):
    all_data=Review.objects.all()
    fav_id=request.session.get("favorite_review")
    fav_obj=all_data.get(pk=fav_id)
    return render(request,'reviews/home.html',{
        'object_list':all_data,
        'fav_obj':fav_obj
    })
def edit(request,slug):
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        temp=Review.objects.get(user_name=slug)
        print(temp.rating)
        form=ReviewForm(instance=temp)
        # print(form.cleaned_data)

    return render(request,'reviews/edit.html',{
        'form':form
    })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"]= "this works!"
        return context
# 1
# def thank_you(request):
#     return render(request,'reviews/thank_you.html')

# class Single(DetailView):
#     template_name = "reviews/detail.html"
#     model = Review
#     # context_object_name = "review"
#

# 1
# class Single(TemplateView):
#     template_name = "reviews/detail.html"
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         review_id=kwargs["id"]
#         ob=Review.objects.get(pk=review_id)
#         context['ob']=ob
#         return context
def single(request,pk):
    ob=Review.objects.get(pk=pk)
    fav_id=int(request.session.get("favorite_review"))
    print(fav_id)
    print(type(fav_id))
    return render(request,'reviews/detail.html',{
        'object':ob,
        'fav_id':fav_id
    })



class AddFavoriteView(View):
    def post(self,request):
        review_id=request.POST["review_id"]
        print(request.POST)
        print(review_id)
        # fav_obj=Review.objects.get(pk=review_id)
        request.session["favorite_review"]=review_id
        return HttpResponseRedirect('/home/'+review_id)

