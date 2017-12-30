#!/usr/bin/python
from operator import itemgetter
import copy

def no_dups(r):
    return len(dict([(i,i) for i in r])) == len(r) and all(a>0 and a<10 for a in r)

def rows_check(mat):
    return all(no_dups(r) for r in mat)

def cols_check(mat):
    return all([True for c in range(len(mat[0])) if no_dups([mat[r][c] for r in range(len(mat))])])

def box_ok(mat, r, c):
    return no_dups([mat[i][j] for i in range(r,r+3) for j in range(c,c+3)])

def boxes_check(mat):
    return all(True for r in range(0,9,3) for c in range(0,9,3) if box_ok(mat,r,c))

def sudoku_solved(mat):
    return rows_check(mat) and cols_check(mat) and boxes_check(mat)
    
def row_peers(mat, r,c):
    return [(r,i) for i in range(len(mat[r])) if i != c]

def col_peers(mat, r,c):
    return [(i,c) for i in range(len(mat)) if i != r]

def box_peers(mat, r,c):
    top_row = int(r/3)*3
    left_col = int(c/3)*3
    return [(i,j) for i in range(top_row,top_row+3,1) for j in range(left_col,left_col+3,1) if not (i==r and j==c)]

def peers(mat, r,c):
    return row_peers(mat,r,c) + col_peers(mat, r,c) + box_peers(mat, r,c)

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

def adjust_peers(m, r,c, vacant):
    #print ('adjusting peers of %d,%d=%d' % (r,c,m[r][c]))
    p = peers(m, r,c)
    for v in vacant:
        ((rx,cx), ch) = v
        if (rx,cx) in p and len(ch)>1:
            v[1] = set(ch) - set([m[r][c]])
            #print ('changed peer (%d,%d) from %s to %s'% (rx,cx, ch, v[1]))
            if len(v[1]) == 1:
                m[rx][cx] = next(iter(v[1]))
                adjust_peers(m, rx,cx, vacant)

#given a position in m, return list of applicable integers
def possibilities(m, r, c):
    return set(range(1,10,1)) - row_numbers(m, r) - column_numbers(m, c) - box_numbers(m,int(r/3)*3,int(c/3)*3)

def ordered_possibilities(m):
    tuples = [[(i,j), possibilities(m, i, j)] for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == -1]
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
    
def solve_with_backtracking(m, backPropagate=False):
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
            if backPropagate:
                adjust_peers(m, r,c, vacant)
            p = solve_with_backtracking(m)
            if p is not None:
                return p
            restore(m, save) 
        return None #no solution    
    else:
        return m #have solution
