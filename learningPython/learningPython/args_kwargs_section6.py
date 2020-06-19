'''
Created on Jun 7, 2020

@author: isgm137
'''
def myfunc(a,b):
    #return 5% of sum of a and b
    return sum((a,b)) * 0.05
print('result ',myfunc(20,5))

def myfunction(*args):

    print(args)
    return sum(args)*0.05
print('result ',myfunction(20,5,5))

def myfunction_1(*args):
    for item in args:
        print(item)
myfunction_1(10,20,30)

#kwargs
def myfunction_2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice{}'.format(kwargs['fruit']))
        print('My fruit of choice{}'.format(kwargs['veggle']))
    else:
        print(' I did not find')
myfunction_2(fruit='apple',veggle='lettuce')
    
def myfunction_3(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would  like {} {}'.format(args[0], kwargs['food']))
myfunction_3(10,20,fruit='banana',food='eggs',animal='dogs')
    
#list whose contain even number
def evenList(*args):
    data_list=[]
    for item in args:
        if item%2==0:
            data_list.append(item)
    return data_list
print('result ',evenList(10,25,30,42,50))

def myfun(string):
    result = []
    for data in range(len(string)):
        if data%2==0:
            result.append(string[data].lower())
        else:
            result.append(string[data].upper())
    return ''.join(result)
print('result',myfun('apple'))

    