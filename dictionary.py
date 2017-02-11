import random
import sys
import os

super_villains = {'General Nuisance':'Nina',
                  'Captain Cold':'Nima',
                  'Death-by-hugs':'Shobha',
                  'Basilisk':'Kannan',
                  'Batman': 'Bruce Wayne'}

print super_villains['Captain Cold']

del super_villains['Batman']

super_villains['Death-by-hugs'] = 'Girija'

print (len(super_villains))

print super_villains

print super_villains.get("General Nuisance")

print super_villains.keys()

print super_villains.values()

# branching is same as c except elif and instead of '{' we use blank lines
# elif in python is used as else if in C

'''syntax:
if condition:
            ...code...
else :
            ...code...

            '''

#or

'''
if condition:
            ...code...
elif :
            ...code...
else :
            ...code...'''

'''C    Python
    &&  and
    ||  or
    !   not'''





