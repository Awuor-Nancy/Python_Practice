from ctypes.wintypes import PINT
from os import PRIO_PGRP


word = "coding"
print(word)

greeting = "hello mercy"
print(len(greeting))

#multiline_string
sentence = '''I am a student at Akirachix and my main goa l is to 
learn how to code so thta one day I can change my family's life and 
get them out of poverty...god help me'''
print(sentence)

#String Concatenation
word = '''I am a student at Akirachix and my main goa l is to 
learn how to code so thta one day I can change my family's life and 
get them out of poverty...god help me'''

name = 'Nancy ou should keep this in mind'
sentence = word + name
print(sentence)

#Escape Sequences in Strings
print('Nancy you should keep this in mind,\t\ and you too')
print('Nancy you should keep this in mind,\n\ and you too')
print('Nancy you should keep this in mind,\a\ and you too')
print('Nancy you should keep this in mind,\' and you too')
print('Nancy you should keep this in mind,\"\ and you too')

#String formatting
radius = 10
pi = 3.142
area = 3.142 * radius **2
print (area)

caution = "Nancy you should keep this in mind"
name = "Awuor"
print(f"I always tell you daily ,{caution} do you hear me ,{name}")

#String Interpolation / f-Strings (Python 3.6+)
a = 4
b = 5
print(f'{a} + {b} / {b} ** {a}')
print(f'{a} - {b} % {b} - {a}')
print(f'{a} * {b} * {b} + {a}')
print(f'{a} // {b} + {b} % {a}')

#Accessing Characters in Strings by Index/Slicing Python Strings
word = "AkiraChix"
print(word [:4])
print(word[2:5])

word = "Organization"
print(word[2:7])
print(word[4:8])
print(word[3:])  #last three

#Reversing a String
greeting = 'Hello, World!'
print(greeting[::-1])

#Skipping Characters While Slicing
greeting = 'Hello, World!'
print(greeting[0:6:2])
print(greeting[4:7])

#String Methods
challenge = 'thirty days of python'
print(challenge.capitalize())
print(challenge.lower())
print(challenge.count('t'))
print(challenge.endswith('A'))
print(challenge.title())

#Replaces tab character with spaces
print(challenge.expandtabs())
print(challenge.find('l'))
#Returns the index of the last occurrence of a substring,
#  if not found returns -1
print(challenge.rfind('d'))

#index(): Returns the lowest index of a substring,
challenge = "Create a website"
sub_string = 'te'
print(challenge.index(sub_string))

#rindex(): Returns the highest index of a substring, 
challenge = "Create a website"
sub_string = 'te'
print(sub_string.rindex('te'))

print(challenge.isalnum())  #Checks alphanumeric character
print(challenge.isalpha())   #Checks alphanumeric character
print(challenge.isdecimal())  

a = '34.8'
#Checks if all characters in a string are numbers (0-9
print(a.isdigit())
#Checks if all characters in a string are decimal (0-9)
print(a.isdecimal())
print(a.isnumeric)
#Checks for a valid identifier - it checks if a string is a valid variable name
print(a.isidentifier) 

careers = ['Html','JS','React','CSS']
result = ''.join(careers)
 #Removes all given characters starting from the beginning and end of the string
print(result.strip)
name = "Nairobary"
print(name.strip('ary'))
print(name.replace("Nairobary",'Kisumu'))

#Splits the string, using given string or space as a separator
city = "London"
print(city.split())
#Converts all uppercase characters to lowercase 
# and all lowercase characters to uppercase characters
city = "GeRMany ROMe"
print(city.swapcase())

word = "Hey man,let's roll"
print(word.startswith("h"))

#Cut(slice) out the first word of Coding For All string.
a = "coding for all"
print(a[0])
print(a.replace('codng',"Python"))
print(a.split('r'))
print(a[0])

#Use index to determine the position of the first occurrence of C in Coding For All.
print(a.index('n'))

#last index
print(a.rindex('l')) 
print(a.rfind('0'))
print(a.rfind('l'))

# Which one of the following variables return
#  True when we use the method isidentifier():
a = '30DaysOfPython'
b =  'thirty_days_of_python'

print(a.isidentifier())
print(b.isidentifier())

#Join the list with a hash with space string.
topic = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(''.join(topic))

#Use the new line escape sequence to separate the following sentences
topic = ['Django', 'Flask', 'Bottle','\t\,Pyramid', 'Falcon']
print(topic)
topic = ['Django', 'Flask', 'Bottle','\n\,Pyramid', 'Falcon']

