#!/usr/bin/env python
# coding: utf-8

import unittest

class TestModule(unittest.TestCase):
    
    def set_up():
        names = get_id()
        all_routes = create_dict(names)
        
    def test_min(self):
        self.asserEqual(min_max(all_routes, "min"), "Line with fewest stops: Blue , 12 ")

    def test_min(self):
        self.asserEqual(min_max(all_routes, "max"), "Line with most stops: Red , count: 22")
    
    def test_algo(self):
        self.asserEqual(search_algorithm("Ashmont", "Arlington"), "['Red', 'Green-C']")
        self.asserEqual(search_algorithm("Bowdoin", "Government Center"), "Blue")
        self.asserEqual(search_algorithm("Sutherland Road", "Cleveland Circle"), "['Green-B', 'Green-C'])

        



