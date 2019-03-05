# Day 3 in Advent of Code

import numpy as np


def part1():
    # Check size to initialiaze array
    rows,cols = 0,0
    for line in data:
        coord = list(map(int, line.split()[2].replace(':','').split(',')))
        kernel = list(map(int, line.split()[3].split('x')))

        rows = int(coord[0]+kernel[0]) if int(coord[0]+kernel[0]) > rows else rows
        cols = int(coord[1]+kernel[1]) if int(coord[1]+kernel[1]) > cols else cols

    matrix = np.zeros((rows, cols))

    # Calculate overlaps
    for line in data:
        location = list(map(int, line.replace(':','').split()[2].split(',')))
        coord = list(map(int, line.split()[3].split('x')))

        matrix[location[0]:location[0]+coord[0], location[1]:location[1]+coord[1]] += 1

    return (np.sum(matrix >= 2), matrix)

def part2(matrix):
    assert matrix.shape != (0,), "Numpy array is empty"
    for line in data:
        #Get values from string
        ID = int(line.split()[0].replace('#', ''))
        coord = list(map(int, line.split()[2].replace(':','').split(',')))
        kernel = list(map(int, line.split()[3].split('x')))

        endRow = int(coord[0]+kernel[0])
        endCol = int(coord[1]+kernel[1])
        
        #Check if claim don't overlap
        elfClaim = matrix[coord[0]:endRow, coord[1]:endCol]
        if elfClaim .shape != (1, 1) and (elfClaim  == 1).all():
            return ID
        elif elfClaim .shape == (1, 1) and elfClaim  == 1:
            return ID
    

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()
    summ , matrix = part1()
    print(f'Answer to part 1 is {summ}')
    ID = part2(matrix)
    print(f'Answer to part 2 is {ID}')
    