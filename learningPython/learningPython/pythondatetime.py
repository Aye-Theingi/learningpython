'''
Created on Jun 18, 2020

@author: isgm137
'''

from datetime import datetime
from datetime import date
today=datetime.today()
print('today',today)
print('today',today.ctime())
myDatetime=datetime(2020,3,12,11,30,0)
print('myDatetime',myDatetime)

date1=date(2020,12,2)
date2=date(2021,12,2)
result=date2-date1
print('type',type(result))
print('total days',result.days)