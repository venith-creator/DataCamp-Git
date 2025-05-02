from django.urls import path
from . import views

app_name = 'VENITHfastcars'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<int:product_id>/detail/', views.product_detail, name='product_detail'),
    path('buy/<int:product_id>/', views.buy, name='buy'),
    path('confirm_purchase/<int:product_id>/', views.confirm_purchase, name='confirm_purchase'),
]