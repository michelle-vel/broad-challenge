#!/usr/bin/env python
# coding: utf-8


#Return Question 2 Answer
names = get_id()
all_routes = create_dict(names)

#get most and least amount of stops for a line
min_max(all_routes, "min")
min_max(all_routes, "max")

#get all stops that connect two or more routes
two_or_more(all_routes)

