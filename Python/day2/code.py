# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:14:29 2019

@author: Issa Hijazi
"""
from collections import Counter
from functools import reduce

def part1():
    frequencies = {}
    for line in inputs:
        charCounter = Counter(line)
        freqAlreadyAdded = {}
        for char in charCounter:
            freq = charCounter[char]
            if not freq in freqAlreadyAdded and freq > 1:
                if freq in frequencies:
                    frequencies[freq] += 1
                else:
                    frequencies[freq] = 1
                freqAlreadyAdded[freq] = True
    return (reduce(lambda x, y: x * y, frequencies.values()))

def optPart1():
    frequencies = {2: 0, 3: 0}
    for line in inputs:
        charCounter = Counter(line)
        frequencies[2] += 1 if 2 in charCounter.values() else 0
        frequencies[3] += 1 if 3 in charCounter.values() else 0
    return (frequencies[2] * frequencies[3])

def part2():
    alreadyCompared = []
    for line in inputs:
        alreadyCompared.append(line)
        for lineX in inputs:
            if lineX in alreadyCompared:
                continue
            else:
                diff = 0
                diffIndex = -1
                for i in range(0, len(line)):
                    if line[i] != lineX[i]:
                        diff += 1
                        diffIndex = i
                    if diff > 1:
                        break
                if diff < 2:
                    return line[:diffIndex] + line[(1+diffIndex):]
def optPart2():
    alreadyCompared = []
    for line in inputs:
        alreadyCompared.append(line)
        for lineX in inputs:
            if lineX in alreadyCompared:
                continue
            else:
                commonChars = [''.join(char1) if char1 == char2 else '' for char1, char2 in zip(line, lineX)]
                if commonChars.count('') < 2:
                    return ''.join(char for char in commonChars if char != '' and char != '\n')
    

with open(("textFile.txt"), "r") as textFile:
    inputs = textFile.readlines()
print(optPart2())