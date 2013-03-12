from unittest import TestCase

from ..solver import Solver
from ..game import *

class TestSolver(TestCase):
    def test_empty_matrix(self):
        matrix = create_empty_game_matrix()
        self.assertFalse(Solver(matrix).has_won('X'))

    def test_rows(self):
        matrix = [['X' for i in range(3)]] +[[EMPTY_SLOT for i in range(3)] for j in range(2)]
        self.assertTrue(Solver(matrix).has_won('X'))

    def test_columns(self):
        matrix = [['X', EMPTY_SLOT, EMPTY_SLOT] for i in range(3)]
        self.assertTrue(Solver(matrix).has_won('X'))

    def test_diagonals(self):
        matrix = [[EMPTY_SLOT for i in range(3)] for j in range(3)]
        for i in range(3):
            matrix[i][i] = 'X'

        self.assertTrue(Solver(matrix).has_won('X'))
