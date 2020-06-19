'''
Created on Jun 9, 2020

@author: isgm137
'''
class Line:
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    
    def slope(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return (y2-y1)/(x2-x1)
c1=(3,2)
c2=(8,10)
myline=Line(c1,c2)
print('distance',myline.distance())
print('slope',myline.slope())

class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return self.height * 3.14 *(self.radius)**2
    def surface_area(self):
        top= 3.14 * (self.radius **2)
        return (2 * top) + (2 * 3.14 * self.radius * self.height)
mycylinder=Cylinder(2,3)
print('volume',mycylinder.volume())
print('surface_area',mycylinder.surface_area())

class Account():
    def  __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,dep_amt):
        self.balance +=dep_amt
        print('Added {dep_amt} to the balance')
    def  withdrawal(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -=wd_amt
            print('Withdrawal Accepted')
        else:
            print('Sorry non enough funds')
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"
            
a=Account('Sam',500)
print('owner',a.owner) 
print('balance',a.balance) 
a.deposit(1100)
a.withdrawal(100)
        
        
