#This program mocks a directory by verifying a directory exists and if not, creates said directory
#Thomas Blankenship

import os

title = "Welcome to the Directory Creator"
author  = "by Thomas Blankenship"
description = "\nPlease enter your credentials & it will be recorded into a text file"


print(title)
print(author)
print(description)

file_name = input("\nFile Name: ")
file_name += '.txt'


file_path = file_name

print('\nFile ',file_name,'has been created.')
print('************************************')

name_first =    input('\n\nFirst Name:\t')
name_last =     input('Last Name:\t')
address =       input('Address:\t')
phone =         input('Phone:\t\t')

with open(file_path, 'w+') as file_object:
    file_object.write(name_first)
    file_object.write(' ')              
    file_object.write(name_last)             
    file_object.write(', ')
    file_object.write(address)
    file_object.write(', ')
    file_object.write(phone)
    
    
with open(file_path) as file_object:
    lines = file_object.readlines()
txt = ""
for line in lines:
    txt += line.rstrip()

print('\nData Entry Verification:')
print('************************************')
print(txt)
