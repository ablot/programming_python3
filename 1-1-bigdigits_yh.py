# -*- coding: utf-8 -*-
"""
@hey2

This is for Python textbook - Chapter 1 - Exercise 1

Print digits as big letters

"""

#%% Import packages
import sys

#%% Which one to run
run_basic = 0
run_num = 1

#%% 
#Set up how to print the digits
Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     * ",
        " *   *  ",
        "  ***   "]

One = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]

Two = [" *** ",
       "*   *",
       "*  * ",
       "  *  ",
       " *   ",
       "*    ",
       "*****"]

Three = [" *** ",
         "*   *",
         "    *",
         " ***",
         "    *",
         "*   *",
         " *** "]

Four = ["   *  ",
        "  **  ",
        " * *  ",
        "*  *  ",
        "******",
        "   *  ",
        "   *  "]

Five = [" *** ",
        "*    ",
        "*    ",
        " *** ",
        "    *",
        "    *",
        " *** "]

Six = [" *** ",
       "*    ",
       "*    ",
       "**** ",
       "*   *",
       "*   *",
       "**** "]

Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         " *   ",
         " *   "]

Eight = [" *** ",
         "*   *",
         "*   *",
         " ***",
         "*   *",
         "*   *",
         " *** "]

Nine = [" ****",
        "*   *",
        "*   *",
        " ****",
        "    *",
        "    *",
        "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
#%%
if run_basic == 1: 
    try:
        whichdigits = sys.argv[1]
        row = 0
        while row < 7:  #loop by row
            line = ""   #empty string
            digitline = ""  #empty string to store digit chars for each line
            column = 0  
            while column < len(whichdigits):  
                number = int(whichdigits[column])
                whichDigit = Digits[number]  #ehich digit figure 
                line += whichDigit[row] + " "  #store the row line of the digit fig
                #print('col='+str(column))
                column += 1
            #print('row='+str(row))
            print(line)
            row += 1
    except IndexError:
        print("usage: in cmd line: 1-1-bigdigits_ans.py <number>")
        print("usage: in spyder console: runfile('1-1-bigdigits_ans.py', args= '<num>'")
    except ValueError as err:
        print(err,"in",whichdigits)
    
#%% 
if run_num == 1:
    try:
        whichdigits = sys.argv[1]
        
        row = 0
        while row < 7:  #loop by row
            line = ""  #empty string to store digit chars for each line
            
            column = 0  
            for column in range(0,len(whichdigits)):  
                number = int(whichdigits[column])
                whichDigit = Digits[number]
                
                #loop through each character of each line of the digit figure
                ichar = 0
                for ichar in range(0,len(whichDigit[row])):
                    whichchar = whichDigit[row][ichar]
                    if whichchar == " ":
                        digitchar = " "
                    elif whichchar == "*":
                        digitchar = str(number)
                    line += digitchar + " "

            print(line)
            row += 1
    except IndexError:
        print("usage: in cmd line: 1-1-bigdigits_ans.py <number>")
        print("usage: in spyder console: runfile('1-1-bigdigits_ans.py', args= '<num>')")
    except ValueError as err:
        print(err,"in",whichdigits)
    
    
    
    