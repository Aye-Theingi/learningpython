'''
Created on Jun 7, 2020

@author: isgm137
'''
def name_function():
    print('Hello')
    
name_function()

def say_Hello(name):
    print('Hello '+name)
    
say_Hello('Aye Theingi')

#add function
def add(n1,n2):
    return n1+n2

result=add(20,30)
print('result ',result)

#find out if the word "dog" is in a string?

def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False
result=dog_check('dog ran away')
print('result ',result)

def dog_check2(mystring):
    return 'dog' in mystring.lower()
result=dog_check2('Dog run away')
print('result ',result)
 
#pig latin
def pig_latin(word):
    firstLetter=word[0]
    #check vowel
    if firstLetter in 'aeiou':
        pig_word=word +'ay'
    else:
        pig_word=word[1:]+firstLetter+'ay'
    return pig_word
result=pig_latin('banana')
print('result '+result)

#coding ex-14(simple math)
def productfun(num1,num2):
    return num1*num2
print('result ',productfun(20, 5))

#coding ex-15(isEven)
def isEvenFun(num):
    if num%2==0:
        return True
    else:
        return False

print('result ',isEvenFun(20))

#coding ex-16(isGreater)
def isGreater(num1,num2):
    if num1>num2:
        return True
    else:
        return False

print('result ',isGreater(20,10))

