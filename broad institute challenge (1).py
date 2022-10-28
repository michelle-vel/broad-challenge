#!/usr/bin/env python
# coding: utf-8

# In[365]:


import requests
import json
from collections import defaultdict


# In[366]:


#the name of where you can board or get off an MBTA subway
# takes in :
    #name - String
    #line - String
    

class Stop():
    def __init__(self, _name):
        self._name = _name 
        self.id = id
    
    def name(self):
        return self._name
        
#route containing multiple stops
# takes in : 
    #name - String
    #stops - list of stop names
    
class Route():
    def __init__(self, _name, _stops):
        self._name = _name
        self._stops = _stops
        self.id = id


    def name(self):
        return self._name
    
    def stops(self):
        return self._stops
    
    def __lt__(self, other):
        return self._name < other._name

    def __eq__(self, other):
        return self._name == other._name and self._stops == other._stops

    
    
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


# In[367]:


#creates adjacency graph without filtering for two or more stops
def all_route(all_routes):
    all_stops = {}
    for route in sorted(all_routes):
        for stop in route.stops():
            name = stop.name()
            if name not in all_stops:
                all_stops[name] = []
                
            (all_stops[name]).append(route.name())
                
    return all_stops


#flips dictionary to return stops for each line
def inverted_dict(d):
    obj = defaultdict(list)
    for key,value in d.items():
        for i in value:
            obj[i].append(key)
    return dict(obj)
    

#finds shortest path between two stops by using modified breadth-first-search
def search_algorithm(stop1, stop2):
    visited_stops = []   
    visited_lines = []
    lines_dict = inverted_dict(adjacency_list)
    
    initial_lines = adjacency_list.get(stop1)
    queue_lines = [[initial_lines]]
    queue_stops = [[stop1]]
    #queue has the first stop 

    s1 = adjacency_list.get(stop1)
    s2 = adjacency_list.get(stop2)
    for i in s1:
        for j in s2:
            if i == j:
                return i

    while queue_stops:
        path = queue_stops.pop(0)
        node = path[-1]
        
        path_lines = queue_lines.pop(0)
        node_lines = path[-1]
        
        #if node is not in visited - so visited must contain STOPS
        #if node is not there we need to go through that stops's lines and find if they contain the destination
        if node not in visited_stops: #and node_lines not in visited_lines:
            
            #the lines of the current node
            
            new_node = adjacency_list[node]
            
            #i is each individual line
            for i in new_node:
                #neighbors is all the stops on that line
                neighbors = lines_dict[i]
            
                #for each stop in that list
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue_stops.append(new_path)
                    
                    new_path_lines = list(path_lines)
                    new_path_lines.append(i)
                    queue_lines.append(new_path_lines)

                    
            
                    if neighbor == stop2:
                        return new_path_lines[1:]
                visited_stops.append(node)
                visited_lines.append(node_lines)
names = get_id()
all_routes = (create_dict(names))
print(all_route(all_routes))
print(search_algorithm("Ashmont", "Arlington"))
print(search_algorithm("Bowdoin", "Government Center"))
print(search_algorithm("Sutherland Road", "Cleveland Circle"))

    


# In[368]:


import unittest


# In[369]:


class TestModule(unittest.TestCase):
    all_routes = 
    def test_min(self):
        min_max(all_routes, arg)

