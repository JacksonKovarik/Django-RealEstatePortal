from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sell', views.sell, name="sell"),
    path('rent', views.rent, name="rent"),
    path('signIn', views.signIn, name="signIn"),
    path('signUp', views.signUp, name="signUp")
]