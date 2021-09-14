# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:19:29 2021

@author: Asus
"""

# calculator for addition and subtraction

print ("1. Add")
print ("2. Subtract")
n= int(input("Enter choice: "))
n1=float(input("Enter number 1: "))
n2=float(input("Enter number 2: "))
if n==1:
    t=n1+n2
    print("The result after adding is ",+t)
    
elif n==2:  
    t= n1-n2
    print ("The result after subtracting is ",+t)

else :
    print ("The choice is invalid")
  