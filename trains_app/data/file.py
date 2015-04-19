import subprocess
pnr = 4519282568
p = subprocess.Popen(['python2.7', '/home/Meghdeep/train_project/trains_app/data/scraper.py', str(pnr) ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print(out)







'''from models import Station

import json
train_file = open("/home/Meghdeep/train_project/trains_app/data/train_route.txt", "r")
output = json.loads(train_file.read())
if( train_file.read() != '[]' ):
    for i in output:
        a = Station.objects.filter( station_name = i )
        if( a.exists() ):
            print( a.station_name )
        else:
            Station.objects.create( station_name = i )
train_file.close()'''