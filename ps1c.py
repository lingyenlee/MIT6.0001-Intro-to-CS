#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:24:38 2019

@author: apple
"""

initial_annual_salary = float(input("Enter your annual salary:"))

semi_annual_raise = 0.07
annual_interest = 0.04
monthly_interest = 0.04/12
total_cost = 1000000
portion_down_payment = 0.25*total_cost
months = 36

current_savings = 0
low = 0
high = 10000
savings_rate = (low+high)/2

numGuess = 0
epsilon = 100

while abs(current_savings - portion_down_payment) >= 100: 
    numGuess += 1
    current_savings = 0
    annual_salary = initial_annual_salary
    
    
    for month in range(1, months+1):
        
        monthly_return = monthly_interest*current_savings
        monthly_contribution =  (savings_rate/10000)*(annual_salary/12)
        current_savings += monthly_return + monthly_contribution
        
        if month % 6 == 0:
            annual_salary += semi_annual_raise*annual_salary
        
    if (current_savings > portion_down_payment):
        high = savings_rate
    else:        
        low = savings_rate
    
    savings_rate = (low+high)/2
   # print("Best savings rate:", savings_rate/10000)
    #print("Steps:", numGuess)
    
    if numGuess > 20:
        break
    

if numGuess > 20:
    print ("It is not possible to make downpayment in 3 years")
else:      
    print("Best savings rate:", savings_rate/10000)
    print("Steps:", numGuess)
    
    

   



   

        


 

