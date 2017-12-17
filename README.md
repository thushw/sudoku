# Sudoku solver

This is a simple sudoku solver that works by recursively trying all possibilities for a cell.
The only optimization it does is to, at each turn, order the number of possibilities for all cells
and pick the first.

The puzzles for testing are taken off [https://www.websudoku.com](https://www.websudoku.com)
Rather than transcribe the values manually, I used [https://jsfiddle.net/thushara/rnj1tetd/2/](https://jsfiddle.net/thushara/rnj1tetd/2/) to build the matrices
in the tests.
To transribe a new puzzle for testing:

1. copy the outerHtml of the table element using a tool like FireBug or Chrome Developer Extension
2. paste that into [https://jsfiddle.net/thushara/rnj1tetd/2/](https://jsfiddle.net/thushara/rnj1tetd/2/) replacing the existing table.
3. Run the fiddle, copy the matrix on the bottom right.

The sudoku puzzles have aptly named 4 categories:

1. Easy
2. Medium
3. Hard
4. Evil


