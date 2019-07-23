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
    #print(transit_distance)
    #print(transit_duration)
    #print(transit_price)
    
    #taxi Trips from baidu map
    url_transit = url_transit0 + ori + des + ak  # transit and taxi
    request_transit = requests.get(url_transit)
    return_transit_parameters = request_transit.json()
    transit_status = return_transit_parameters['status']
    # The distance, duaration, price of taxi
    taxi_routes = return_transit_parameters['result']['taxi']
    if transit_status == 0 and transit_routes !=[]:
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
    #print(taxi_distance)
    #print(taxi_duration)
    #print(taxi_price)
    taxi_info = str(taxi_distance) + ',' + str(taxi_duration) + ',' + str(taxi_price)
    with open('C:\\Users\\LAYZ\\Desktop\\taxi.csv', 'a',encoding= 'utf-8') as f:
            f.write(taxi_info)
            f.write('\n')
            f.close()
    continue
    
    #riding trips from baidu map
    
    url_riding = url_riding0 + ori + des + ak + riding_type
    request_riding = requests.get(url_riding)
    return_riding_parameters = request_riding.json()
    #The distance,duration of riding 
    riding_status = return_riding_parameters['status'] 
    riding_routes = return_riding_parameters['result']

    if riding_status ==0 and riding_routes !=[]:
        riding_distance = riding_routes['routes'][0]['distance']
        riding_duration = riding_routes['routes'][0]['duration']
    else:
        riding_distance = 0
        riding_duration = 0

    riding_info = str(riding_distance) + ',' + str(riding_duration)     
    with open('C:\\Users\\LAYZ\\Desktop\\riding.csv', 'a',encoding= 'utf-8') as f:
        f.write(riding_info)
        f.write('\n')
        f.close()
    continue
    #print(riding_distance)
    #print(riding_duration)
    
    # the distance, duration of url_driving
    url_driving = url_driving0 + ori + des + ak
    request_driving = requests.get(url_driving)
    return_driving_parameters = request_driving.json()
    driving_status = return_driving_parameters['status']
    driving_routes = return_driving_parameters['result']
    # the distance, duration, price of driving_routes
    if driving_status ==0 and driving_routes!=[]:        
        driving_distance = driving_routes['routes'][0]['distance']
        driving_duration = driving_routes['routes'][0]['duration']
    else:
        driving_distance = 0
        driving_duration = 0
    driving_info = str(driving_distance) + ',' + str(driving_duration)   
    with open('C:\\Users\\LAYZ\\Desktop\\driving.csv', 'a',encoding= 'utf-8') as f:
        f.write(driving_info)
        f.write('\n')
        f.close()
    continue
    # print(driving_distance)
    # print(driving_duration)
    
    url_walking = url_walking0 + ori + des + ak
    request_walking = requests.get(url_walking)
    return_walking_parameters = request_walking.json()
    walking_status = return_walking_parameters['status']
    walking_routes = return_walking_parameters['result']
    # the distance, duration, price of walking_routes
    if walking_status ==0 and walking_routes!=[]:        
        walking_distance = walking_routes['routes'][0]['distance']
        walking_duration = walking_routes['routes'][0]['duration']
    else:
        walking_distance = 0
        walking_duration = 0
    walking_info = str(walking_distance) + ',' + str(walking_duration) 
        
    with open('C:\\Users\\LAYZ\\Desktop\\walking.csv', 'a',encoding= 'utf-8') as f:
        f.write(walking_info)
        f.write('\n')
        f.close()
    continue

       