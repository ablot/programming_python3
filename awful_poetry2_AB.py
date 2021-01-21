#!/usr/bin/env python3
import random
import sys

articles = ['a', 'the']
subjects = ['tractor', 'pear', 'car', 'laddle', 'mug', 'flower']
verbs = ['sang', 'ran', 'drives', 'flies', 'stole']
adverbs = ['awsomely', 'rapidely', 'silently', 'mechanically']

err_msg = 'Unvalid arguments. Enter a number between 1 and 10'
error = False
try:
    num_lines = int(sys.argv[1])
except ValueError as err:
    print(err_msg)
    error = True
    num_lines = 1
except IndexError:
    num_lines = 5

if (num_lines > 10) or (num_lines < 1):
    error = True
    print(err_msg)

if not error:
    for _ in range(num_lines):
        sentence = random.choice(articles) + ' ' + random.choice(subjects)
        sentence = sentence + ' ' + random.choice(verbs)
        if random.randint(0,1):
            sentence = sentence + ' ' + random.choice(adverbs)
        print(sentence)
