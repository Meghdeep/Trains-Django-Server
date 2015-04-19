from django.shortcuts import render
import requests
import os
from data.models import User, Vendor, Food_Order, Passenger, Station
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

def index( request ):
    return HttpResponse("Hello you're at the DataBase Index !")

def user_table( request, name_id_in ):
    return_value = serializers.serialize("json", User.objects.filter( user_id = name_id_in ) )
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

def station_list(request, pnr):
    import json
    from subprocess import call
    call(["python2.7", "scraper.py", str(pnr)])
    train_file = open("/home/Meghdeep/train_project/trains_app/data/train_route_mod.txt", "r")
    output = json.loads(train_file.read())
    return HttpResponse(json.dumps(output))

# WITNESS THE GRAVEYARD OF STUFF THAT WAS ATTEMPTED TO GET THIS FUCKING THING TO WORK -.-''
# AND IT'S NOT EVEN A COMPREHENSIVE LIST OF ALL THE STUFF THAT WAS ATTEMPTED >_<
    #from subprocess import call
    #call(["python2.7", "scrapy_scraper.py", str(pnr)])
    #train_file = open("train_route_mod.txt", "r")
    #train_file.encode('
    #output = json.loads(train_file.read())
    #output = train_file.read()
    #for i in output:
    #    if( ( Station.objects.filter(station_name=i) ).count == 0 ):
    #        Station.objects.create(station_name=i)
    #return HttpResponse(output)
    #return HttpResponse(output)

    #import json
    #r = requests.get( "http://Raghav.pythonanywhere.com/scraper/proxy/" + str(pnr) )
    #output = r.json()
    #output = json.loads(output)

    #import subprocess
    #from subprocess import Popen, PIPE
    #process = Popen(['swfdump', '/tmp/filename.swf', '-d'], stdout=PIPE, stderr=PIPE)
    #stdout, stderr = process.communicate()
    #sh.swfdump("python2.7", "scraper.py", str(pnr))
    #from subprocess import Popen
    #output = subprocess.check_output(['python2.7', 'scraper.py', str(pnr)])
    #train_file = open("train_route_mod.txt", "r")
    #output = train_file.read()
    #output = output.decode('utf-8')
    #output = json.loads(output)

    #import re, json
    #res = requests.post( 'http://www.getpnrstatus.co.in?pnrno=' + str(pnr) )
    #page = res.text.encode('utf8')
    #response = Selector( text = page )
    #p = response.xpath('//td/text()').extract()
    #train_num = p[1].strip()    # Train Number for Specific PNR Obtained
    #res = requests.get('http://runningstatus.in/status/'+train_num+'-today')
    #page = res.text.encode('utf8')
    #response = Selector( text = page )
    #train_list = []
    #for row in response.xpath('//tbody/tr'):
	#    col = row.xpath('.//td/text()').extract()
	#    train_list.append(str(re.search(r'(.*)[(]',col[0]).group(1)))
    #return HttpResponse(json.dumps(train_list))
