from django.urls import path
from . import views
urlpatterns=[
    path('<month>/',views.monthly_challenge,name='monthly_challenge'),

]