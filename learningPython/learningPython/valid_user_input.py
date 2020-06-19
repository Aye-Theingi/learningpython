'''
Created on Jun 8, 2020

@author: isgm137
'''
def user_choice():
    choice="WRONG"
    acceptable_range=range(0,10)
    within_range=False
    while choice.isdigit()==False or within_range ==False:
        choice=input('Enter number(0-10)')
        if choice.isdigit == False:
            print('Sorry that is not digit')
        if  choice.isdigit()==True:
            if int(choice) in acceptable_range:
                within_range=True
            else:
                print('Sorry, you are out of acceptable range(0-10)')
                within_range=False
    return int(choice)
user_choice()