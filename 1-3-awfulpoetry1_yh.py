#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 23:22:56 2021

@author: hey2

This is for Python textbook - Chapter 1 - Exercise 3

"""
#%% Import modules
import random

#%%
runs = 5
structures = 2

articles = ["the ", "a ", "an ", "another "]
subjects = ["cat ", "dog ", "man ", "woman "]
verbs = ["sang ", "run ", "jumped ", "laughed ", "hoped "]
adverbs = ["loudly ", "quietly ", "well ", "badly "]

for irun in range(0,runs):
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    
    whichSent = random.randint(1,structures)
    
    if whichSent == 1:
        sentence = article + subject + verb + adverb
    elif whichSent == 2:
        sentence = article + subject + verb
    
    print(sentence)
    