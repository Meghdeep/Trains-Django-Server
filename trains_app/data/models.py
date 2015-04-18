from django.db import models

# Create your models here.

class Train(models.Model):
    train_no = models.CharField(primary_key=True, max_length=200)
    train_name = models.CharField(max_length=200)
    def __str__(self):
        return '%s - %s'%(str(self.train_no),str(self.train_name))

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    user_password = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
#    category = ( ('A','First AC'), ('B','Second AC'), ('C','Third AC'), ('D','Sleeper') )
    def __str__(self):
        return '%s - %s'%(str(self.user_id),str(self.name))

class Station(models.Model):
    station_id = models.CharField(primary_key=True, max_length=200)
    station_name = models.CharField(max_length=200)
    def __str__(self):
        return '%s - %s'%(str(self.station_id),str(self.station_name))

#class Destination(models.Model):
#    destination_id = models.AutoField(primary_key=True)
#    destination_name = models.CharField(max_length=200)

#class Route(models.Model):
#    route_id = models.CharField(primary_key=True, max_length=200)
#    train_no = models.ForeignKey(Train)
#    seq_no = models.CharField(max_length=200)
#    station_id = models.ForeignKey(Station)
#    arrival_time = models.DateTimeField('Arrival Date Time')
#    departure_time = models.DateTimeField('Departure Date Time')
#    delay = models.TimeField('Delay Time')
#    def __str__(self):
#        return '%s'%(str(self.route_id))

#class Taxi(models.Model):
#    taxi_no = models.CharField(primary_key=True, max_length=200)
#    car_type = ( ('A','Mini'), ('B','Sedan'), ('C','Prime') )
#    station_id = models.ForeignKey(Station)
#    rate = models.CharField(max_length=200)
#    def __str__(self):
#        return '%s' % (str(self.taxi_no))

#class Cab_Order(models.Model):
#    cab_order_id = models.AutoField(primary_key=True)
#    taxi_id = models.Key(Taxi)
#    user_id = models.ForeignKey(User)
#    station_id = models.ForeignKey(Station)
#    destination_id = models.ForeignKey(Destination)
#    pickup = models.DateTimeField('Pickup Date Time')
#    def __str__(self):
#        return '%s - Taxi: %s PicksUp User: %s' % (str(self.cab_order_id),str(self.taxi_id),str(self.user_id))

class Vendor(models.Model):
    vendor_id = models.CharField(primary_key=True, max_length=200)
    shop_name = models.CharField(max_length=200)
    station_id = models.ForeignKey(Station)
    menu = models.CharField(max_length=200)
    def __str__(self):
        return '%s - %s' % (str(self.vendor_id),str(self.shop_name))

class Food_Order(models.Model):
    food_order_id = models.AutoField(primary_key=True)
    vendor_id = models.ForeignKey(Vendor)
    user_id = models.ForeignKey(User)
    order_made = models.CharField(max_length=200)
    def __str__(self):
        return '%s - from Vendor: %s Sells to User: %s' % (str(self.food_order_id),str(self.vendor_id),str(self.user_id))

class Passenger(models.Model):
    pnr = models.CharField(primary_key=True, max_length=200)
    user_id = models.ForeignKey(User)
#    cab_order_id = models.CharField(Cab_Order)
    food_order_id = models.ForeignKey(Food_Order)
#    route_id = models.ForeignKey(Route)
#    notification_id = models.CharField(max_length=200)
    passenger_source = models.ForeignKey(Station)
    passenger_destination = models.CharField(max_length=200)
    def __str__(self):
        return '%s' % (str(self.pnr))