import random
import sys
import os

def addnumber(fnum, lnum):
    sumnum = fnum + lnum
    return sumnum

print addnumber(1,4)

name = sys.stdin.readline()

print "Hello", name

print name[0:2]

print name[-2:]

print name[:-2]

print name.capitalize()
