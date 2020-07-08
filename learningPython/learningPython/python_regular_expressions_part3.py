'''
Created on Jun 21, 2020

@author: isgm137
'''
import re
re.search(r'cat|dog','The cat is here')

result=re.findall(r'.at','The cat in the hat sat there.')
print('result',result)
result_space=re.findall(r'...at','The cat in the hat went splat.') #... means space
print('result_space',result_space)

result_num=re.findall(r'^\d','2 is a number')
print('result_num',result_num)
    
result_num1=re.findall(r'\d$','The number is 2')
print('result_num1',result_num1)

pharse='there are 3 numbers 34  inside 5 this sentence'
pattern=r'[^\d]+'
print('pharse',re.findall(pattern,pharse))

test_pharse='This is a string! But it has punctuation.How can we remove it?'
clean=re.findall(r'[^!.?]+', test_pharse)

print('result',clean)
print(''.join(clean))

