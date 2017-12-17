#!/usr/bin/python
import unittest
import sudoku

class TestSudoku(unittest.TestCase):
    def test_easy(self):
        m = \
        [[7,-1,-1,-1,-1,9,-1,2,1],
         [-1,8,5,1,2,-1,-1,-1,-1],
         [1,2,3,7,-1,-1,9,-1,-1],
         [-1,-1,-1,-1,6,2,-1,-1,4],
         [6,4,-1,-1,-1,-1,-1,3,8],
         [5,-1,-1,3,1,-1,-1,-1,-1],
         [-1,-1,9,-1,-1,7,6,1,5],
         [-1,-1,-1,-1,5,3,2,7,-1],
         [2,5,-1,6,-1,-1,-1,-1,3]]
        p = sudoku.solve_with_backtracking(m)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

    def test_medium(self):
        m = \
            [[-1,-1,-1,9,5,-1,1,-1,3],
             [3,-1,2,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,4,3,-1,6,7],
             [1,-1,-1,-1,9,-1,-1,5,-1],
             [-1,-1,3,-1,8,-1,9,-1,-1],
             [-1,8,-1,-1,3,-1,-1,-1,2],
             [6,4,-1,8,1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,5,-1,1],
             [7,-1,1,-1,2,5,-1,-1,-1]]
        p = sudoku.solve_with_backtracking(m)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

    def test_hard(self):
        m = \
            [[-1,3,-1,2,-1,-1,6,7,-1],
             [-1,-1,-1,-1,-1,-1,8,-1,-1],
             [-1,2,-1,-1,3,-1,-1,-1,-1],
             [-1,-1,-1,9,7,-1,-1,4,-1],
             [3,4,-1,8,-1,1,-1,9,5],
             [-1,8,-1,-1,5,4,-1,-1,-1],
             [-1,-1,-1,-1,1,-1,-1,8,-1],
             [-1,-1,1,-1,-1,-1,-1,-1,-1],
             [-1,6,7,-1,-1,2,-1,5,-1]]
        p = sudoku.solve_with_backtracking(m)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

    def test_evil(self):
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
        p = sudoku.solve_with_backtracking(m)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSudoku)
    unittest.TextTestRunner(verbosity=2).run(suite)
