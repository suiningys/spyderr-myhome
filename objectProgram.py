# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 22:10:26 2017

@author: Administrator
"""

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
        
    def printScore(self):
        print('%s %s' %(self.name, self.score))
        
    def getScore(self):
        if self.score>90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'
        
haogang = Student('Lihaogang',90)
ziyang = Student('Shenziyang',59)
haogang.girlFriend = 3

class Animal(object):
    def run(self):
        print('animal is running...')
        
class Dog(Animal):
    def run(self):
        print('dog is running...')
        
class Cat(Animal):
    def run(self):
        print('cat is running...')

dog = Dog()
cat = Cat()

dog.run()
cat.run()
def run_twice(animal):
    animal.run()
    animal.run()
    
run_twice(dog)