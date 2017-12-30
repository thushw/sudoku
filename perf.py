#!/usr/bin/python
import sudoku
import time

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


def timeit(f, backPropagate):
    t0 = time.time()
    for i in range(1000):
        f(backPropagate)
    t1 = time.time()
    total = t1-t0
    return total

print ('time to solve without backPropagation %d' % timeit(evil, False))
print ('time to solve with backPropagation %d' % timeit(evil, True))
