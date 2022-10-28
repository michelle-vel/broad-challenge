#!/usr/bin/env python
# coding: utf-8


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

