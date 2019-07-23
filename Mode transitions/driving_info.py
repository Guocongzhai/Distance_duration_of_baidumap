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
url_driving0 = 'http://api.map.baidu.com/directionlite/v1/driving?'
url_walking0 = 'http://api.map.baidu.com/directionlite/v1/walking?'
ak0 = 'your key'
ak = '&ak=' + ak0
riding_type = '&riding_type=0'
#parameter setting
for trip in testdata:
    #ori and des 
    ori = '&origin=' + str(trip[4]) + ',' + str(trip[3]) #origin
    des = '&destination=' + str(trip[6]) + ',' + str(trip[5]) #destination 
    url_driving = url_driving0 + ori + des + ak
    request_driving = requests.get(url_driving)
    return_driving_parameters = request_driving.json()
    driving_status = return_driving_parameters['status']
    # the distance, duration, price of driving_routes
    if driving_status == 0:
        driving_routes = return_driving_parameters['result']['routes']
        if driving_routes !=[]:       
            driving_distance = driving_routes[0]['distance']
            driving_duration = driving_routes[0]['duration']
        else:
            driving_distance = 0
            driving_duration = 0    
    else:
        driving_distance = 0
        driving_duration = 0
    driving_info = str(driving_distance) + ',' + str(driving_duration)   
    with open('C:\\Users\\LAYZ\\Desktop\\driving.csv', 'a',encoding= 'utf-8') as f:
        f.write(driving_info)
        f.write('\n')
        f.close()
    continue  