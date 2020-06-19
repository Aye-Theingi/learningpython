'''
Created on Jun 8, 2020

@author: isgm137
'''
game_list=[0,1,2]
def display_game(game_list):
    print('here is the current list:')
    print(game_list)
display_game(game_list)

def position_choice():
    choice="WRONG"
    while choice not in ['0','1','2']:
        choice=input('Pick  a position(0,1,2)')
        if choice not in ['0','1','2']:
            print('sorry,invalid choice')
        else:
            print('Choice',choice)
    return int(choice)
position_choice()

#replace string
def replacement_choice(game_list,position):
    user_replacement=input('Enter a string  to place at position')
    game_list[position]=user_replacement
    return game_list

result=replacement_choice(game_list,1)
print('The replacement',result)

def gameon_choice():
    choice="wrong"
    while choice not in ['Y','N']:
        choice=input('Keep playing(Y or N)')
        if choice not in ['Y','N']:
            print('Sorry, I do not understand,please choose Y or N')
    if choice=="Y":
        return True
    else:
        return False
print('The result',gameon_choice())

game_on=True
while game_on:
    display_game(game_list)
    position=position_choice()
    game_list=replacement_choice(game_list, position)
    display_game(game_list)
    game_on=gameon_choice()