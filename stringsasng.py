# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:41:08 2021

@author: Asus
"""

#strings

print("hello")
print('hello')
a="welcome"
print(a) #assign string to variable
print(len(a)) #length of string
b=""" hello world.
act as if what you do makes
a change.
IT DOES """
print(b) #multiline strings
c=''' hello world.
act as if what you do makes
a change.
IT DOES '''
print(c) #using single quotes
print("makes" in c) #check string
print("if" not in c) #check if not
d="Hello, World!"
print(d[1])  #gets the character at position 1
print(len(d))
if "," in d:
    print("y") #Checking str
print(d[:5])  #slice from start
print(d[2:]) # slice to the end
print(d[-6:-1]) #negative indexing(doesnt include -1)
print(d.upper()) #prints the string in uppercase
print(d.lower()) #prints the str in lower case

e=" Hello , World "
print(e.strip()) #REMOVES SPACE FROM BEGINNING AND END
print(e.replace("e","i")) #replaces a str with another
print(e.split(",")) #split string
f= a+" "+d  #concatenation
print (f)

age=19
tx="my name is mona, and i am {} "
print(tx.format(age)) #str format*
Q=3
IT=567
pp=49.98
myorder="i want to pay {2} for {0} pieces of item {1}."
print(myorder.format(Q,IT,pp)) #FORMAT*
txt="we are the so called \"vikings\" from north." #escape char
print(txt)

for x in "banana":
    print(x)  #looping in string
