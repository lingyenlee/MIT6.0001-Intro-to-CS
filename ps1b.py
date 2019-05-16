#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:54:12 2019

@author: apple
"""

annual_salary = float(input("Enter your annual salary:"))
semi_annual_raise = float(input("Enter your raise as decimal:"))
portion_saved = float(input("Enter the portion saved:"))
total_cost = float(input("Enter the cost of your dream home:"))

month = 0
current_savings = 0
monthly_savings = annual_salary/12
portion_down_payment = 0.25*total_cost


while current_savings <= portion_down_payment:
    
    monthly_savings = annual_salary/12
    current_savings += portion_saved*monthly_savings + current_savings*0.04/12
    month += 1 
    
    #conditions for increase should be after the calculation, increase
    #happen after multiples of 6
    if month % 6 == 0:
        annual_salary += semi_annual_raise*annual_salary
    
       
print("Number of months:", month)