'''
Created on Jun 19, 2020

@author: isgm137
'''
import re
text="The agent's phone number  is 408-555-1234."
result= 'phone' in text
print('result',result)
pattern='phone'
resultsearch=re.search(pattern,text)
print('resultsearch',resultsearch)
pattern='NOT IN TEXT'
searchresult=re.search(pattern,text)
print('searchresult',searchresult)

print(resultsearch.span())
print(resultsearch.start())
print(resultsearch.end())


text='my phone once,my phone twice'
searchpattern='phone'
textsearch=re.findall(searchpattern, text)
print('textsearchresult',textsearch)
print('length_searchtext',len(textsearch))
for match in re.finditer(searchpattern, text):
    print(match.group())

