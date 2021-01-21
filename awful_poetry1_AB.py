#!/usr/bin/env python3
import random

articles = ['a', 'the']
subjects = ['tractor', 'pear', 'car', 'laddle', 'mug', 'flower']
verbs = ['sang', 'ran', 'drives', 'flies', 'stole']
adverbs = ['awsomely', 'rapidely', 'silently', 'mechanically']

for _ in range(5):
    sentence = random.choice(articles) + ' ' + random.choice(subjects)
    sentence = sentence + ' ' + random.choice(verbs)
    if random.randint(0,1):
        sentence = sentence + ' ' + random.choice(adverbs)
    print(sentence)
