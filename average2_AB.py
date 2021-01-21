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

# Bubble sort
debug = False
ori_numbers = numbers[:]
n = len(numbers)
fully_ordered = False
while not fully_ordered:
    fully_ordered = True
    pivot = 0
    index = 1
    while pivot < (n - 1):
        do_switch = False
        if debug:
            print('new pivot %s @ %s'%(numbers[pivot], pivot))
        while numbers[pivot] > numbers[index]:
            if debug:
                print('    next index %s @ %s'%(numbers[index], index))
            do_switch = True
            index = index + 1
            if index == n:
                break
        # switch pivot and index
        if do_switch:
            fully_ordered = False
            num = numbers[index-1]
            numbers[index-1] = numbers[pivot]
            numbers[pivot] = num
            if debug:
                print('Switch them. New list: %s'%numbers)
        pivot = index
        index = pivot + 1
    if debug:
        print('Try again')

print('sorted: %s\n' % numbers)

if len(numbers):
    if n == 1:
        median = numbers[0]
    else:
        ind_mid = n / 2
        if str(ind_mid)[-1] == '5':
            median = numbers[int(ind_mid)]
        else:
            ind_mid = int(ind_mid-0.5)
            median = (numbers[ind_mid] + numbers[ind_mid+1])/2
            
    print('count: ' + str(len(numbers)) + ', sum: ' + str(running_sum) +
    ', lowest ' + str(lowest) + ', highest ' + str(highest) + ', average ' + 
    str(running_sum/len(numbers)) + ', median: ' + str(median))