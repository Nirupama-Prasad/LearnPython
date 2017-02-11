import random
import sys
import os

class Animal:
    __name = " "
    __height = 0
    __weight = 0
    __sound = 0
    '''none is NULL
        you dont need constructors to initialize
        __ means private
        '''

    # Contructor -_-
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    #       self = this
    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_sound(self, sound):
            self.__sound = sound

    def set_weight(self, weight):
            self.__weight = weight

    def get_name(self, name):
        return self.__name

    def get_height(self, height):
        return self.__height

    def get_sound(self, sound):
         return self.__sound

    def get_weight(self, weight):
        return self.__weight

    def get_type(self):
        print "Animal"

    def toString(self):
        print self.__name
        print self.__height
        print self.__sound
        print self.__weight
        return "%s is %d cm tall, %d kgs and says %s" % (self.__name, self.__height, self.__weight, self.__sound)


Girl = Animal('Nina', 159, 55, 'DisgAsting')

print Girl.toString()


#Inheritance
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self, owner):
        return self.__owner

#Method Overloading
    def toString(self):
        return "%s is %d cm tall, %d kgs and says %s. Her Owner is " % (self.__name, self.__height,
                                                         self.__weight,
                                                         self.__sound,
                                                        self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print self.get_sound()
        else:
            print self.get_sound() * how_many

Spot = Dog("Spot", 53, 27, "Ruff", "Nina")

print Spot.toString()

'''Polymorphism

class AnimalTesting:
        def.get_Type(Girl)
            animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(Girl)
test_animals.get_type(spot)

Spot.multipleSounds(4)
            '''


