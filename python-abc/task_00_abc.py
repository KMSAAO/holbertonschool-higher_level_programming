#!/usr/bin/python3
"""
This file provide a abstract Animal
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """This is the abstract class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """This is the subclass of Animal and return Bark"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """This is the subclass of Animal and return Meow"""
    def sound(self):
        return "Meow"
