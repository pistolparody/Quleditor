import pygame as pg


class Enumerator:
    __counter = 0
    __label = None

    def __init__(self , number:int,data=None,label=None):
        self.number = number
        self.data = data
        self.label = label

    def __str__( self ):
        return "[EnumObject : ( <number:{}> , <data:{}> ) ]".format(self.number,self.data)

    @staticmethod
    def reset(label:str=None):
        Enumerator.__label = label
        Enumerator.__counter += 1

    @staticmethod
    def get_next(data=None):
        Enumerator.__counter += 1
        return Enumerator(Enumerator.__counter,data,Enumerator.__label)



Enumerator.reset()

InvalidColorValue = Enumerator.get_next("The color values must be between 0 and 255!")
InvalidScale = Enumerator.get_next("The scale value must be between 0 and 1! ")











