# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

annual_salary = float(input("Enter your annual salaray:"))
portion_saved = float(input("Enter the portion saved:"))
total_cost = float(input("Enter the cost of your dream home:"))

month = 0
current_savings = 0
monthly_savings = annual_salary/12
portion_down_payment = 0.25*total_cost


while current_savings <= portion_down_payment:
    current_savings += portion_saved*monthly_savings + current_savings*0.04/12
    month += 1

print("Number of months:", month)