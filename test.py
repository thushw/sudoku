#!/usr/bin/python
import unittest
import sudoku

class TestSudoku(unittest.TestCase):
    def test_easy_no_backtrack(self):
        self.easy(False, False)

    def test_easy_simple(self):
        self.easy(True, False)

    def test_easy_back_propagate(self):
        self.easy(True, True)

    # def test_medium_no_backtrack(self):
    #     self.medium(False, False)

    def test_medium_simple(self):
        self.medium(True, False)

    def test_medium_back_propagate(self):
        self.medium(True, True)

    def test_hard_simple(self):
        self.hard(True, False)

    def test_hard_back_propagate(self):
        self.hard(True, True)

    def test_evil_simple(self):
        self.evil(True, False)

    def test_evil_back_propagate(self):
        self.evil(True, True)

    def test_aiescargot_simple(self):
        self.aiescargot(True, False)

    def test_aiescargot_back_propagate(self):
        self.aiescargot(True, True)

    def test_artoincala_simple(self):
        self.artoincala(True, False)

#    def test_artoincala_back_propagate(self):
#        self.artoincala(True, True)

    def solve_with_asserts(self, m, backTrack, backPropagate):
        if backTrack:
            p = sudoku.solve_with_backtracking(m, backPropagate)
        else:
            p = sudoku.solve(m)
        self.assertTrue(p is not None)
        self.assertTrue(sudoku.sudoku_solved(p))
        self.assertTrue(sudoku.sudoku_solved(m))

    def easy(self, backTrack, backPropagate):
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
        self.solve_with_asserts(m, backTrack, backPropagate)

    def medium(self, backTrack, backPropagate):
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
        self.solve_with_asserts(m, backTrack, backPropagate)

    def hard(self, backTrack, backPropagate):
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
        self.solve_with_asserts(m, backTrack, backPropagate)

    def evil(self, backTrack, backPropagate):
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
        self.solve_with_asserts(m, backTrack, backPropagate)

    def aiescargot(self, backTrack, backPropagate):
        #https://usatoday30.usatoday.com/news/offbeat/2006-11-06-sudoku_x.htm
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
        self.solve_with_asserts(m, backTrack, backPropagate)

    def artoincala(self, backTrack, backPropagate):
        #http://www.mirror.co.uk/news/weird-news/worlds-hardest-sudoku-can-you-242294
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
        self.solve_with_asserts(m, backTrack, backPropagate)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSudoku)
    unittest.TextTestRunner(verbosity=2).run(suite)
