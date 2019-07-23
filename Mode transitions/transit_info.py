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
#parameter setting
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
        # The distance, duaration, price of transit
        if transit_status == 0:
            transit_routes = return_transit_parameters['result']['routes']
            if transit_routes !=[]:
                transit_distance = transit_routes[0]['distance']  # m
                transit_duration = transit_routes[0]['duration']  # s
                transit_price = transit_routes[0]['price']  # yuan
            else:
                transit_distance = 0  # m
                transit_duration = 0  # s
                transit_price = 0  # yuan
        else:
            transit_distance = 0  # m
            transit_duration = 0  # s
            transit_price = 0  # yuan

        transit_info = str(transit_distance) + ',' + str(transit_duration) + ',' + str(transit_price)
        with open('C:\\Users\\LAYZ\\Desktop\\transit.csv', 'a+',encoding= 'utf-8') as f:
            f.write(transit_info)
            f.write('\n')
            f.close()
        continue
    except:
        time.sleep(3)
        transit_distance = 0  # m
        transit_duration = 0  # s
        transit_price = 0  # yuan 
        with open('C:\\Users\\LAYZ\\Desktop\\transit.csv', 'a+',encoding= 'utf-8') as f:
            f.write(transit_info)
            f.write('\n')
            f.close()
        continue
