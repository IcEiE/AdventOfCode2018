# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:12:43 2019

@author: Issa Hijazi
"""
def part1():
    return(sum(map(int, inputs)))

def part2():
    frequencies = {}
    currentSum = 0
    ints = list(map(int, inputs))
    while(True):
        for line in ints:
            currentSum += int(line)
            if currentSum in frequencies:
                return currentSum
            frequencies[currentSum] = True
            
with open(("day1.txt"), 'r') as txtFile:
    inputs = txtFile.readlines()

print("Day 1 Part 1: ", part1())
print("Day 1 Part 2: ", part2())