#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 22:36:30 2021

@author: hey2

This is for Python textbook - Chapter 1 - Exercise 2

Keep taking number from user input before pressing Enter key to terminate

"""
running = 1

nums = []

i = 0
while running:
    which_num = input("enter a number or Enter to finish: ")
    nums.append(which_num)  #append newly entered num into the list
    
    i+=1
    
    if not which_num:  #if nothing is entered (only pressed the Enter key)
        nums.remove('')  #remove the last empty element of the list
        print("numbers: " + str(nums))
        
        #nums = map(int,nums_ls)
            
        count = len(nums)
        sum = sum(int(num) for num in nums)
        min = min(int(num) for num in nums)
        max = max(int(num) for num in nums)
        mean = sum/count
        print("count = " + str(count) \
              + " sum = " + str(sum) \
              + " lowest number = " + str(min) \
              + " highest number = " + str(max) \
              + " mean = " + str(mean)) 
            
        break

        
