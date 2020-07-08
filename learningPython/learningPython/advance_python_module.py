'''
Created on Jun 29, 2020

@author: isgm137
'''
import shutil
shutil.unpack_archive('hello.zip', '','zip')
with open('hellotesting/hello.txt') as file:
    content=file.read()
    print('content is ',content)