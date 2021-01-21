#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 22:36:30 2021

@author: hey2

This is for Python textbook - Chapter 1 - Exercise 5

Sorting to find median

"""

import math


running = 1

nums_ls = []

i = 0
while running:
    which_num = input("enter a number or Enter to finish: ")
    nums_ls.append(which_num)  #append newly entered num into the list
    
    i+=1
    
    if not which_num:  #if nothing is entered (only pressed the Enter key)
        nums_ls.remove('')  #remove the last empty element of the list
        print("numbers: " + str(nums_ls))
        nums = [int(num) for num in nums_ls] #Convert list of string to list of int
        
        # Bubble sort
        inum = 0
        itime = 0
        for itime in range(0,len(nums)):  #go through the list for num of elements
            for inum in range(0,(len(nums)-1)):  #compare left and right num
                num1 = nums[inum]
                num2 = nums[inum+1]
                if num1 > num2:
                    nums[inum] = num2
                    nums[inum+1] = num1
            itime+=1
        
        print("numbers: " + str(nums))
        if (len(nums)%2) == 1:
            median = nums[math.floor(len(nums)/2)]
        else:
            median = int((nums[int(len(nums)/2)-1]+nums[int(len(nums)/2)])/2)
        print("median: " + str(median))
                
        
        break

        
