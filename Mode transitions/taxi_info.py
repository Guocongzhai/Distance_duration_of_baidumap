#encoding:utf-8
import csv
import json
from datetime import datetime
import time
import requests

#read file
testdata = csv.reader(open('C:\\Users\\LAYZ\\Desktop\\testdata.csv',encoding='utf-8'))
#url setting 
url_transit0 = 'http://api.map.baidu.com/direction/v2/transit?'  # transit and taxi
url_riding0 = 'http://api.map.baidu.com/direction/v2/riding?'
url_driving0 = 'http://api.map.baidu.com/direction/v2/driving?'
url_walking0 = 'http://api.map.baidu.com/directionlite/v1/walking?'
ak0 = 'your key'
ak = '&ak=' + ak0
riding_type = '&riding_type=0'

for trip in testdata:
    #ori and des 
    ori = '&origin=' + str(trip[4]) + ',' + str(trip[3]) #origin
    des = '&destination=' + str(trip[6]) + ',' + str(trip[5]) #destination   
    #transit and taxi Trips from baidu map
    url_transit = url_transit0 + ori + des + ak  # transit and taxi
    request_transit = requests.get(url_transit)
    return_transit_parameters = request_transit.json()
    transit_status = return_transit_parameters['status']
    try:
        # The distance, duaration, price of taxi
        if transit_status == 0 :
            taxi_routes = return_transit_parameters['result']['taxi']
            if taxi_routes !=[]:
                taxi_distance = taxi_routes['distance']
                taxi_duration = taxi_routes['duration']
                triptime = datetime.strptime(trip[8],'%Y/%m/%d %H:%M')
                #print(triptime.hour)
                if 23>triptime.hour>6:
                    taxi_price = taxi_routes['detail'][0]['total_price']
                else:
                    taxi_price = taxi_routes['detail'][1]['total_price']
            else:
                taxi_distance = 0
                taxi_duration = 0
                taxi_price = 0 
        else: 
            taxi_distance = 0
            taxi_duration = 0
            taxi_price = 0 
        #print(taxi_distance)
        #print(taxi_duration)
        #print(taxi_price)
        taxi_info = str(taxi_distance) + ',' + str(taxi_duration) + ',' + str(taxi_price) 
        with open('C:\\Users\\LAYZ\\Desktop\\taxi.csv', 'a',encoding= 'utf-8') as f:
                f.write(taxi_info)
                f.write('\n')
                f.close()
        continue
    except:
        time.sleep(3)
        taxi_distance = 0
        taxi_duration = 0
        taxi_price = 0
        with open('C:\\Users\\LAYZ\\Desktop\\taxi.csv', 'a',encoding= 'utf-8') as f:
            f.write(taxi_info)
            f.write('\n')
            f.close()
        continue
        