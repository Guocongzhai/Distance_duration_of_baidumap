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
url_riding0 = 'http://api.map.baidu.com/directionlite/v1/riding?'
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
    url_riding = url_riding0 + ori + des + ak + riding_type
    request_riding = requests.get(url_riding)
    return_riding_parameters = request_riding.json()
    #The distance,duration of riding 
    riding_status = return_riding_parameters['status'] 
    
    if riding_status ==0 :
        riding_routes = return_riding_parameters['result']['routes']
        if riding_routes != []:
            riding_distance = riding_routes[0]['distance']
            riding_duration = riding_routes[0]['duration']
        else:
            riding_distance = 0
            riding_duration = 0
    else:
        riding_distance = 0
        riding_duration = 0

    riding_info = str(riding_distance) + ',' + str(riding_duration)     
    with open('C:\\Users\\LAYZ\\Desktop\\riding.csv', 'a',encoding= 'utf-8') as f:
        f.write(riding_info)
        f.write('\n')
        f.close()
    continue   