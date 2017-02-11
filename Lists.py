import random
import sys
import os

grocery_list = ["Tomatoes", "curd", "Onions", "Chillies"]

print "First item : ", grocery_list[0]

other_events = ["Call doctor", "Meet doctor", "Print documents"]

events = [other_events, grocery_list]

print events

events.append('Redo Statement')

grocery_list.insert(1, 'tuna')

grocery_list.remove('tuna')

grocery_list.sort()

grocery_list.reverse()

del grocery_list[3]

print events