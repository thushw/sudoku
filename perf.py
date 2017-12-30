#!/usr/bin/python
import sudoku
from timeit import Timer as T

def evil(backPropagate):
    m = \
        [[8,-1,-1,7,-1,-1,1,-1,-1],
         [-1,-1,-1,-1,-1,-1,3,-1,-1],
         [-1,-1,6,1,4,-1,-1,8,-1],
         [7,-1,-1,-1,-1,5,-1,3,-1],
         [3,-1,5,-1,-1,-1,2,-1,1],
         [-1,6,-1,3,-1,-1,-1,-1,8],
         [-1,5,-1,-1,8,1,9,-1,-1],
         [-1,-1,4,-1,-1,-1,-1,-1,-1],
         [-1,-1,1,-1,-1,2,-1,-1,6]]
    p = sudoku.solve_with_backtracking(m, backPropagate)


print ('solving without back propagation...')
print (T(lambda: evil(False) ).repeat(repeat=1, number = 1000))
print ('solving with back propagation...')
print (T(lambda: evil(True) ).repeat(repeat=1, number = 1000))
