'''
Created on Jun 19, 2020

@author: isgm137
'''
import re
text='My phone number is 408-555-1234'
phone=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print('phone',phone.group())
phone=re.search(r'\d{3}-\d{3}-\d{4}', text)
print('phone1',phone.group())
phone_result=re.compile(r'\d{3}-\d{3}-\d{4}')
results=re.search(phone_result, text)
print('result',results.group())
