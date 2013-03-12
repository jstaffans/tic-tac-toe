from unittest import TestCase
from tictactoe import has_won
__author__ = 'johannes'

class TestHas_won(TestCase):
    def test_empty_matrix(self):
        matrix = [['' for i in range(3)] for j in range(3)]
        self.assertFalse(has_won('X', matrix))

    def test_rows(self):
        matrix = [['X' for i in range(3)]] +[['' for i in range(3)] for j in range(2)]
        self.assertTrue(has_won('X', matrix))

    def test_columns(self):
        matrix = [['X', '', ''] for i in range(3)]
        self.assertTrue(has_won('X', matrix))

    def test_diagonals(self):
        matrix = [['' for i in range(3)] for j in range(3)]
        for i in range(3):
            matrix[i][i] = 'X'

        self.assertTrue(has_won('X', matrix))
