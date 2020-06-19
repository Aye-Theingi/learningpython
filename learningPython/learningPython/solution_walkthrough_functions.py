'''
Created on Jun 15, 2020

@author: isgm137
'''

class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total -=self.bet
# asking user for integer input.This would be a good place to use try/except.
def take_bet(chips):
    while  True:
        try:
            chips.bet= int(input("How many chips would like to bet?"))
        except:
            print('Sorry please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry,your bet cannot exceed.You have {}'.format(chips.total))
            else:
                break
        finally:
            print('Your bet is {}'.format(chips.bet))
            
chips=Chips()
take_bet(chips)
            