#!/usr/bin/env python
# coding: utf-8
import requests
import json
from collections import defaultdict

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
    names = get_id()
    all_routes = create_dict(names)
    adjacency_list = all_route(all_routes)
    lines_dict = inverted_dict(adjacency_list)
    
    initial_lines = adjacency_list.get(stop1)
    queue_lines = [[initial_lines]]
    queue_stops = [[stop1]]
    #queue has the first stop 

    s1 = adjacency_list.get(stop1)
    s2 = adjacency_list.get(stop2)
    
    if s1 == None or s2 == None:
        return "invalid stops"
    
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
        if node not in visited_stops: 
            
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
    
    if new_path_lines == []:
        return "path not found"


