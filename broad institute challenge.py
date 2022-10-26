#!/usr/bin/env python
# coding: utf-8

# In[321]:


import requests
import json


# In[333]:


# Question 1
#Write a program that retrieves data representing all, what we'll call "subway" routes: "Light Rail"
#(type 0) and “Heavy Rail” (type 1). The program should list their “long names” on the console.

#Partial example of long name output: Red Line, Blue Line, Orange Line...

#There are two ways to filter results for subway-only routes. Think about the two options below
#and choose:

#1. Download all results from https://api-v3.mbta.com/routes then filter locally
#2. Rely on the server API (i.e., https://api-v3.mbta.com/routes?filter[type]=0,1) to
#filter before results are received

#Please document your decision and your reasons for it

#option 1: download all results and then filter
#TO DO: document decision


#the name of where you can board or get off an MBTA subway
# takes in :
    #name - String
    #line - String
    

class Stop():
    def __init__(self, name):
        self.name = name        
    
    def get_name(self):
        return self.name
        
#route containing multiple stops
# takes in : 
    #name - String
    #stops - list of stop names
    #count = number of stops
    
    #TO DO: user should not be able to change count and potentially input an incorrect number
    
class Route():
    def __init__(self, name, stops, count):
        self.name = name
        self.stops = stops
        self.count = count

    
    def get_name(self):
        return self.name
    
    def get_stops(self):
        return self.stops

    def get_count(self):
        return self.count

    def __eq__(self, other):
        return self.name == other.rank and self.stops == other.stops and self.count == other.count
    
    def __lt__(self, other):
        return self.count < other.count
    
    

def get_data_routes(url):
    r = requests.get(url)
    ret = json.loads(r.text)
    return ret

def get_stops(name):
    request = "https://api-v3.mbta.com/stops?filter[route]={}".format(name)
    all_stops = get_data_routes(request)
    return all_stops


#returns a list of all long names
def get_long_names():
    ret = get_data_routes("https://api-v3.mbta.com/routes?filter[type]=0,1")    
    list_names = []
    total = ret["data"]
    for i in range(len(total)):
        curr = total[i]["attributes"]["long_name"]
        list_names.append(curr)
    return list_names

get_long_names()
#returns a list of all route IDs
def get_id():
    ret = get_data_routes("https://api-v3.mbta.com/routes?filter[type]=0,1")    
    list_names = []
    total = ret["data"]
    for i in range(len(total)):
        curr = total[i]["id"]
        list_names.append(curr)
    return list_names    
    
#TO DO: test functions
get_id()


# Question 2
#1. The name of the subway route with the most stops as well as a count of its stops.
#2. The name of the subway route with the fewest stops as well as a count of its stops
#3. A list of the stops that connect two or more subway routes along with the relevant route
#names for each of those stops.


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
    return Route(name, create_object_stop(name), len(create_object_stop(name)))

#create ALL routes - take in list of names (from get_id function)
def create_dict(route_list):
    final_list = []
    for i in route_list:
        route = create_route(i)
        final_list.append(route)
        
    #d = dict.fromkeys((Route.name for Route in final_list), (Route.stops for Route in route_list), (Route.count for Route in route_list))
    return final_list

#returns routes with the most/fewest stops
def min_max(all_routes):
    r_sorted = sorted(all_routes)
    print("Line with fewest stops:", min(r_sorted).get_name(), ", count:", min(r_sorted).get_count())
    print("Line with most stops:", max(r_sorted).get_name(), ", count:", max(r_sorted).get_count())

#returns all stops that connect 2 or more routes and the respective routes
def two_or_more(all_routes):
    all_stops = {}
    for route in sorted(all_routes):
        
        for stop in route.get_stops():
            name = stop.get_name()
            if name not in all_stops:
                all_stops[name] = []
                
            (all_stops[name]).append(route.get_name())
    two = {}
    
    for key in all_stops:
        if len(all_stops[key]) >= 2:
            two[key] = all_stops[key]
    return two

#all_routes = create_dict(names)
#two_or_more(all_routes)


# In[ ]:





##IGNORE BELOW



def create_dict():
    list_stops = get_stops()

    d = dict.fromkeys((Stop.line for Stop in list_stops))
    
    for key in d:
        name = []
        for Stop in list_stops:
            if Stop.get_line() == key:
                name.append(Stop.get_name())
                d[key] = name
    return d



def create_routes():
    #for each line (red, mattapan, orange, green, blue) have the Route be "name" of the line
    #and list of each of the stops 
    current_dict = create_dict()
    list_route = []
    for key in current_dict:
        count = len(current_dict[key])
        route = Route(key, current_dict[key], count)
        list_route.append(route)
    #print([Route.name for Route in list_route])
    #print([Route.stops for Route in list_route])
    #print([Route.count for Route in list_route])

    return list_route


def min_max():
    list_routes = create_routes()
    r_sorted = sorted(list_routes)
    
    print("Line with fewest stops:", min(r_sorted).get_name(), ", count:", min(r_sorted).get_count())
    print("Line with most stops:", max(r_sorted).get_name(), ", count:", max(r_sorted).get_count())


#loop to generate stops for all lines and save in a list
def create_all_stops():
    all_stops = get_id()
    stop_list = []
    for i in all_stops:
        curr = create_object_stop(i)
        stop_list.append(curr)
    return stop_list

print(create_all_stops())





# In[ ]:




