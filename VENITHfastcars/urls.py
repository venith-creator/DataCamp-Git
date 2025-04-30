from django.urls import path
from . import views



#/VENITHfastcars
#/VENITHfastcars/1/detail
#/VENITHfastcars/new

urlpatterns = [
    path('', views.index ),
    path('new', views.new)
]