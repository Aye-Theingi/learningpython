'''
Created on Jun 9, 2020

@author: isgm137
'''
class Error_Excep:
    try:
        result=10+ 10
       
    except:
        print('Hey it looks like you are not  adding correctly')
    else:
        print('result',result)
Error_Excep.result


def ask_for_int():
    while True:
        try:
            result=int(input("Please provide numbers"))
        except:
            print('That is not a number')
            continue
        else:
            print('Thank you')
            break
        finally:
            print('End of try/except/finally')
ask_for_int()

def square():
    #wariting for correct response
    waiting =True
    while waiting:
        try:
            n=int(input('Enter a number'))
        except:
            print('Please try again')
            continue
        else:
            break
    print("Your number squared is", n ** 2)
square()
