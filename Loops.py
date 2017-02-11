import random
import sys
import os

for x in range(0, 10):
    print x, ' '

grocery_list = ["Tuna", "Onions", " Chillies", "Tomatoes"]

for y in grocery_list:
    print y

for x in [2, 4, 6, 8, 10]:
    print x

num_list = [[1,2,3],[10,20,30], [100,200,300]]

for x in [0,1,2]:
    for y in [0,1,2]:
        print num_list[x][y]

random_num = random.randrange(0,100)

while random_num != 15:
    print random
    random_num = random.randrange(0, 100)


