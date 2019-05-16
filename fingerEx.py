# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = int(input("Enter a positive integer: "))
pwr = 1
root = 0
check = 0

while root**pwr < abs(x):
    while pwr < 6: 
        if root**pwr == x:
            print("Root is:", root)
            print("Power is:", pwr)
            check = 1
            break
        pwr += 1
    root += 1
    pwr = 1
    
if check != 1:
    print("No such combination")

 
    
    