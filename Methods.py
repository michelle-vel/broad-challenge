#!/usr/bin/env python
# coding: utf-8

# In[ ]:


url_stops = "https://api-v3.mbta.com/routes?filter[type]=0,1"

def get_data_routes(url):
    API_KEY = "507a3ef6cad24cf29ca83f563e63bf2a"
    r = requests.get(url, headers={"x-api-key": API_KEY})
    ret = json.loads(r.text)    
    return ret

def get_stops(name):
    request = "https://api-v3.mbta.com/stops?filter[route]={}".format(name)
    all_stops = get_data_routes(request)
    return all_stops

#def error():
    

#returns a list of all route IDs
def get_id():
    ret = get_data_routes(url_stops)    
    list_names = []
    total = ret["data"]
    for i in range(len(total)):
        curr = total[i]["id"]
        list_names.append(curr)
    return list_names    

#returns a list of all long names
def get_long_names():
    ret = get_data_routes("https://api-v3.mbta.com/routes?filter[type]=0,1")    
    list_names = []
    total = ret["data"]
    for i in range(len(total)):
        curr = total[i]["attributes"]["long_name"]
        list_names.append(curr)
    return list_names

#returns stops for ONE line, in the form of list and NOT stop object
def make_stops(name):    
    all_stop = get_stops(name)
    total = all_stop["data"]
    list_stops = []
    for i in range(len(total)):
        curr = total[i]["attributes"]["name"]
        list_stops.append(curr)
    return list_stops

#creates stop objects for ONE line
def create_object_stop(name):
    stop_list = []
    for i in make_stops(name):
        stop = Stop(i)
        stop_list.append(stop)
    return stop_list

#create route for ONE line
def create_route(name):
    return Route(name, create_object_stop(name))

#create ALL routes - take in list of names (from get_id function)
def create_dict(route_list):
    final_list = []
    for i in route_list:
        route = create_route(i)
        final_list.append(route)
        
    return final_list

#returns routes with the most/fewest stops
def min_max(all_routes, arg):
    r_sorted = sorted(all_routes)
    if arg == "min":
        print("Line with fewest stops:", min(r_sorted).name(), ", count:", len(min(r_sorted).stops()))
    
    if arg == "max":
        print("Line with most stops:", max(r_sorted).name(), ", count:", len(max(r_sorted).stops()))
    
#returns all stops that connect 2 or more routes and the respective routes
def two_or_more(all_routes):
    all_stops = {}
    for route in sorted(all_routes):
        
        for stop in route.stops():
            name = stop.name()
            if name not in all_stops:
                all_stops[name] = []
                
            (all_stops[name]).append(route.name())
    two = {}
    
    for key in all_stops:
        if len(all_stops[key]) >= 2:
            two[key] = all_stops[key]
    return two

