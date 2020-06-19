'''
Created on Jun 15, 2020

@author: isgm137
'''
import random
from django.db.models.sql.constants import SINGLE
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
        'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing=True

class Card:
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
    def __str__(self):
        return self.ranks + " of "+self.suits

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp +='\n' +card.__str__()
        return "The deck has:"+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
test_deck=Deck()
# print('Test Deck',test_deck)
test_deck.shuffle()
# print('shuffle_deck',test_deck)

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.ranks]
        #track aces
        if card.ranks =="Ace":
            self.aces +=1
    def adjust_for_ace(self):
        #if  total  value >21 and  I still have an ace
        # Than change my ace to be A 1  instead of AN 11
        while self.value >21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
      
#player  
test_player=Hand()
#deal 1 card from the deck card
pulled_card=test_deck.deal()
print('pulled card',pulled_card)
test_player.add_card(pulled_card)
print('test_hand',test_player)
print('test_player',test_player.value)


        