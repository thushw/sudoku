#!/usr/bin/python
from operator import itemgetter
import copy

def no_dups(r):
    return len(dict([(i,i) for i in r])) == len(r) and all(a>0 and a<10 for a in r)

def rows_check(mat):
    return all(no_dups(r) for r in mat)

def cols_check(mat):
    for c in range(len(mat[0])):
        l = []
        for r in range(len(mat)):
            l.append(mat[r][c])
        if not no_dups(l):
            return False
    return True

def box_ok(mat, r, c):
    l = []
    for i in range(r,r+3):
        for j in range(c,c+3):
            l.append(mat[i][j])
    return no_dups(l)        

def boxes_check(mat):
    for r in range(0,9,3):
        for c in range(0,9,3):
            if not box_ok(mat,r,c):
                return False
    return True
    
def sudoku_solved(mat):
    return rows_check(mat) and cols_check(mat) and boxes_check(mat)
    
def row_numbers(m, r):
    return set(m[r])

def column_numbers(m, c):
    s = set([])
    for r in range(len(m)):
        s.add(m[r][c])
    return s

def box_numbers(m,r,c):
    s = set([])
    for i in range(r,r+3,1):
        for j in range(c,c+3,1):
            s.add(m[i][j])
    return s

#given a position in m, return list of applicable integers
def possibilities(m, r, c):
    return set(range(1,10,1)) - row_numbers(m, r) - column_numbers(m, c) - box_numbers(m,int(r/3)*3,int(c/3)*3)

def ordered_possibilities(m):
    tuples = [((i,j), possibilities(m, i, j)) for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == -1]
    return sorted(tuples, key=lambda x: len(x[1]))

def solve(m):
    vacant = ordered_possibilities(m)
    changed = True
    while len(vacant) > 0 and changed:
        changed = False
        ((r,c), choices) = vacant[0]
        if len(choices) == 1:
            m[r][c] = next(iter(choices))
            vacant = ordered_possibilities(m)
            changed = True
    return m

def to_be_filled(m):
    return sum(1 for r in range(len(m)) for c in range(len(m[r])) if m[r][c] == -1)


def restore(to, fr):
    for i in range(len(fr)):
        for j in range(len(fr[i])):
            to[i][j] = fr[i][j]
    
def solve_with_backtracking(m):
    if not sudoku_solved(m):
        #we may mod the puzzle, but we may hit a dead end and have to restore it
        #for the caller - so save it first
        save = copy.deepcopy(m)
        vacant = ordered_possibilities(m)
        if len(vacant) == 0:
            print (m)
            print("still %d to be filled %s" % (to_be_filled(m), sudoku_solved(m)))
            return None #no solution
        ((r,c), choices) = vacant[0]
        for choice in choices:
            m[r][c] = choice
            p = solve_with_backtracking(m)
            if p is not None:
                return p
            restore(m, save) 
        return None #no solution    
    else:
        return m #have solution
