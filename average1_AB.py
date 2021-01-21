#!/usr/bin/env python3
numbers = []
running_sum = 0
lowest = None
highest = None
while True:
    entry = input('enter a number or Enter to finish: ')
    if not entry:
        break
    try:
        number = int(entry)
        numbers.append(number)
        running_sum += number
        if (highest is None) or (number > highest):
            highest = number
        if (lowest is None) or (number < lowest):
            lowest = number
    except ValueError as err:
        print(err)
print('numbers: %s\n'%numbers)

if len(numbers):
    print('count: ' + str(len(numbers)) + ', sum: ' + str(running_sum) +
    ', lowest ' + str(lowest) + ', highest ' + str(highest) + ', average ' + 
    str(running_sum/len(numbers)))