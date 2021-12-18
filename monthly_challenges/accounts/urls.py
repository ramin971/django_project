from django.urls import path,include
from . import views

urlpatterns=[
    path('login/',views.user_login, name='log_in'),
    path('',include('django.contrib.auth.urls')),

]
