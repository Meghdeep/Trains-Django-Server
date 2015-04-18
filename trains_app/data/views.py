from django.shortcuts import render
import requests
import os
from data.models import User, Vendor, Food_Order, Passenger
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

def index( request ):
    return HttpResponse("Hello you're at the DataBase Index !")

def user_table( request, name_in ):
    return_value = serializers.serialize("json", User.objects.filter( name = name_in ) )
    return HttpResponse(return_value)

#def test(request):
#    r = requests.get( "http://seproject.site11.com/seProject/ShortestDistance.php?longitude=93.5348466&latitude=26.11111111&id=1" )
#    #urllib.request.urlopen('http://seproject.site11.com/seProject/ShortestDistance.php?longitude=93.5348466&latitude=26.11111111&id=1')
#    return HttpResponse(r.text)

def distance( request,id, latitude, longitude ):
    #payload = {'id' : id, 'latitude': latitude, 'longitude': longitude}
    requests.get("http://seproject.site11.com/seProject/ShortestDistance.php?id=%s&latitude=%s&longitude=%s"%(id,latitude,longitude))
    return HttpResponse()

#def station(request, pnr_in):
#    return_value = serializers.serialize("json", Route.objects.filter( pnr = pnr_in ) )
#    return HttpResponse(return_value)

def shop_list( request, station_id_in ):
    return_value = serializers.serialize("json", Vendor.objects.filter( station_id = station_id_in) )
    return HttpResponse(return_value)

def shop_menu( request, vendor_id_in ):
    return_value = Vendor.objects.filter( vendor_id = vendor_id_in )
    return HttpResponse(return_value)

def enter_food_order( request, pnr_in, vendor_id_in, user_id_in, order_in ):
    current = Food_Order.objects.create(vendor_id=vendor_id_in, user_id=user_id_in, order_made=order_in)
    return_value = Passenger.objects.filter(pk=pnr_in).update(food_order_id=current.pk)
    return HttpResponse(return_value.pk)

def what_was_ordered(request, order_in):
    return_value = Food_Order.objects.filter(pk=order_in)
    return HttpResponse(return_value)

def create_new_user( request, name_in, phone_number_in, user_password_in, email_in ):
    User.objects.create(user_id=phone_number_in, name=name_in, phone_number=phone_number_in, user_password=user_password_in, email=email_in )
    return HttpResponse()

def station_lister( request, pnr_in ):
    os.system("python scraper.py " + str(pnr_in) )
    return HttpResponse()