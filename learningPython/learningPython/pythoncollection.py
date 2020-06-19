'''
Created on Jun 17, 2020

@author: isgm137
'''
from collections import Counter
from collections import namedtuple
mylist=[1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3]
print('count',Counter(mylist))
mylist1=['a','a',10,11,11]
print('Count',Counter(mylist1))
mysentence="How many times does each word show up in this sentence with a word"
print('split string',mysentence.split())
print('count split string',Counter(mysentence.split()))


Dog=namedtuple('Dog',['age','breed','name'])
summary=Dog(age=5,breed="Husky",name='Sam')
print('type ',type(summary))
print('Dog',summary)
print('age',summary.age)
print('breed',summary.breed)
print('name',summary.name)


