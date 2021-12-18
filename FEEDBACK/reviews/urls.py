from django.urls import path
from . import views
urlpatterns=[
    path('',views.ReviewView.as_view()),
    # path('home/',views.Home.as_view(),name='home'),
    path('home/',views.home,name='home'),
    path('home/favorite/',views.AddFavoriteView.as_view()),
    path('home/<int:pk>',views.single),
    path('home/<slug:slug>',views.edit,name='edit'),
    path('thank-you',views.ThankYouView.as_view(),name='thank'),

]
