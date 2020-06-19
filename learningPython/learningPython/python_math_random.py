'''
Created on Jun 19, 2020

@author: isgm137
'''
import math
from math import pi
import random
value=4.35

print('floor value',math.floor(value))
print('ceil value',math.ceil(value))
print('round value',round(value))
print('round value2',round(5.5))

print('pi value',pi)
print('math_e value',math.e)
print('math_log_e value',math.log(math.e))
print('math_log value',math.log(100,10))
sin_value=math.sin(10)
print('sin value',sin_value)
degree_value=math.degrees(pi/2)
print('degree_value',degree_value)
radian_value=math.radians(180)
print('radian_value',radian_value)
randomvalue=random.randint(0,100)
print('random_value',randomvalue)

mylist=list(range(0,20))
print(mylist)
print('random_choice_value',random.choice(mylist))
randomdata1=random.choices(population=mylist,k=10)
print('sample with replacement',randomdata1)
randomdata2=random.sample(population=mylist,k=10)
print('sample without replacement',randomdata2)
randomshuffle=random.shuffle(mylist)
print('random shuffle',randomshuffle)



