from django.contrib import admin
from data.models import User, Train, Station
#from data.models import Destination, Route, Taxi, Cab_Order
from data.models import Vendor, Food_Order, Passenger
#from data.models import User
# Register your models here.

admin.site.register(User)
admin.site.register(Train)
admin.site.register(Station)
#admin.site.register(Destination)
#admin.site.register(Route)
#admin.site.register(Taxi)
#admin.site.register(Cab_Order)
admin.site.register(Vendor)
admin.site.register(Food_Order)
admin.site.register(Passenger)
