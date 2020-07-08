'''
Created on Jun 29, 2020

@author: isgm137
'''
import time
import timeit
def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str,range(n)))
#current time before
start_time=time.time()
#run code
result=func_one(1000000)
# current time after running code
end_time=time.time()
elapse_time=end_time - start_time
print('elapse time',elapse_time)

stmt=''' 
func_one(100) 
'''
setup=''' 
def func_one(n):
    return [str(num) for num in range(n)]
    '''
print(timeit.timeit(stmt, setup, number=100000))

