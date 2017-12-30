#!/usr/bin/python
import unittest
import sudoku

class TestSudoku(unittest.TestCase):
    def test_easy_simple(self):
        self.easy(False)

    def test_easy_back_propagate(self):
        self.easy(True)

    def test_medium_simple(self):
        self.medium(False)

    def test_medium_back_propagate(self):
        self.medium(True)

    def test_hard_simple(self):
        self.hard(False)

    def test_hard_back_propagate(self):
        self.hard(True)

    def test_evil_simple(self):
        self.evil(False)

    def test_evil_back_propagate(self):
        self.evil(True)

    def test_aiescargot_simple(self):
        self.aiescargot(False)

    def test_aiescargot_back_propagate(self):
        self.aiescargot(True)

    def test_artoincala_simple(self):
        self.artoincala(False)

#    def test_artoincala_back_propagate(self):
#        self.artoincala(True)

    def easy(self, backPropagate):
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
        p = sudoku.solve_with_backtracking(m, backPropagate)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

    def medium(self, backPropagate):
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
        p = sudoku.solve_with_backtracking(m, backPropagate)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

    def hard(self, backPropagate):
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
        p = sudoku.solve_with_backtracking(m, backPropagate)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

    def evil(self, backPropagate):
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
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

    def aiescargot(self, backPropagate):
        m = \
            [[ 8, 5,-1,-1,-1, 2, 4,-1,-1],
             [ 7, 2,-1,-1,-1,-1,-1,-1, 9],
             [-1,-1, 4,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1, 1,-1, 7,-1,-1, 2],
             [ 3,-1, 5,-1,-1,-1, 9,-1,-1],
             [-1, 4,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1, 8,-1,-1, 7,-1],
             [-1, 1, 7,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1, 3, 6,-1, 4,-1]]
        p = sudoku.solve_with_backtracking(m, backPropagate)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

    def artoincala(self, backPropagate):
        m = \
            [[-1,-1, 5, 3,-1,-1,-1,-1,-1],
             [ 8,-1,-1,-1,-1,-1,-1, 2,-1],
             [-1, 7,-1,-1, 1,-1, 5,-1,-1],
             [ 4,-1,-1,-1,-1, 5, 3,-1,-1],
             [-1, 1,-1,-1, 7,-1,-1,-1, 6],
             [-1,-1, 3, 2,-1,-1,-1, 8,-1],
             [-1, 6,-1, 5,-1,-1,-1,-1, 9],
             [-1,-1, 4,-1,-1,-1,-1, 3,-1],
             [-1,-1,-1,-1,-1, 9, 7,-1,-1]]
        p = sudoku.solve_with_backtracking(m, backPropagate)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSudoku)
    unittest.TextTestRunner(verbosity=2).run(suite)
