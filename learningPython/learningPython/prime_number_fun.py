'''
Created on Jun 7, 2020

@author: isgm137
'''
def count_primes(num):
    #check input 0 or 1
    if num<2:
        return 0
    #greater than 2
    primes=[2]
    x=3
    while x<=num:
        # check if x is prime or not
        for y in primes:
            if x%y ==0:
                x+=2
                break
            
        else:
            primes.append(x)
            x+=2
    print(primes)
    return len(primes)
print('result ',count_primes(100))