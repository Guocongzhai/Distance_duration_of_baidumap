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
    url_walking = url_walking0 + ori + des + ak
    request_walking = requests.get(url_walking)
    return_walking_parameters = request_walking.json()
    walking_status = return_walking_parameters['status']
    # the distance, duration, price of walking_routes
    if walking_status ==0 : 
        walking_routes = return_walking_parameters['result']['routes'] 
        if walking_routes != []:      
            walking_distance = walking_routes[0]['distance']
            walking_duration = walking_routes[0]['duration']
        else:
            walking_distance = 0
            walking_duration = 0
    else:
        walking_distance = 0
        walking_duration = 0
    walking_info = str(walking_distance) + ',' + str(walking_duration) 
        
    with open('C:\\Users\\LAYZ\\Desktop\\walking.csv', 'a',encoding= 'utf-8') as f:
        f.write(walking_info)
        f.write('\n')
        f.close()
    continue