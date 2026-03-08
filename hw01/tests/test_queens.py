import unittest
from src.queens import solve_n_queens

class TestNQueens(unittest.TestCase):
    def test_4_queens(self):
        solutions = solve_n_queens(4)
        self.assertEqual(len(solutions), 2)  # 4皇后有2种解

    def test_8_queens(self):
        solutions = solve_n_queens(8)
        self.assertEqual(len(solutions), 92)  # 8皇后有92种解

if __name__ == '__main__':
    unittest.main()
