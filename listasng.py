# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:07:20 2021

@author: Asus
"""

# 1.1 list-ordered, changeable and allows duplicate

list1= ["pi","eta","alpha","apple","kiwi","mango","lis"]
print(list1)   #prints the list
print(len(list1))  #prints the length of list
print(type(list1)) # prints the type of data type
print(list1[1])   #prints the second element
print(list1[-1]) #negative indexing means it starts from end
print (list1[2:5])  #prints range-2:5 starts at 2 and prints upto 4
print(list1[:5])   #Prints upto 5 (not including 5)
print(list1[2:])
print(list1[-5:-1])
#checking item is present or not
if "kiwi" in list1:
    print("yes")
    
li2 = list(("p", "e", "a"))
print(li2)
