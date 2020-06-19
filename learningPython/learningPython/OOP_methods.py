'''
Created on Jun 8, 2020

@author: isgm137
'''
class Dog():
    species='mammal'
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
#         print('Breed',self.breed)
#         print('Name',self.name)
        
        
    def bark(self):
        print("Wolf,My name is {}".format(self.name))
my_dog=Dog('Lab','Frankie')
print('Species',my_dog.species)
print('Breed',my_dog.breed)
print('Name',my_dog.name)
my_dog.bark()



class Circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius * radius * self.pi
    def get_circumference(self):
        return self.radius * self.pi *2
my_circle=Circle()
print('PI',my_circle.pi)
print('get_circumference',my_circle.get_circumference())
print('area',my_circle.area)
    
    