from unittest import TestCase

from ..game import *

class TestGame(TestCase):

    def test_x_has_first_turn(self):
        game = Game()

        self.assertRaises(IllegalActionException, game.place_marker, 'O', 0, 0)

        game.place_marker('X', 0, 0)
        expected_matrix = create_empty_game_matrix()
        expected_matrix[0][0] = 'X'
        self.assertEqual(expected_matrix, game.get_matrix())

    def test_illegal_symbol_as_marker(self):
        game = Game()
        self.assertRaises(IllegalActionException, game.place_marker, 'Y', 0, 0)

    def test_matrix_boundaries(self):
        game = Game()

        self.assertRaises(IllegalActionException, game.place_marker, 'X', -1, 0)
        self.assertRaises(IllegalActionException, game.place_marker, 'X', 0, 3)
        self.assertRaises(IllegalActionException, game.place_marker, 'X', 3, 3)
        self.assertRaises(IllegalActionException, game.place_marker, 'X', 0, -1)

    def test_occupied_slot(self):
        game = Game()
        game.place_marker('X', 0, 0)
        game.place_marker('O', 1, 0)
        self.assertRaises(IllegalActionException, game.place_marker, 'X', 1, 0)

    def test_game_ending(self):
        game = Game()
        self.assertFalse(game.game_ended())

        game.place_marker('X', 0, 0)
        game.place_marker('O', 0, 1)
        game.place_marker('X', 1, 0)
        game.place_marker('O', 1, 1)

        self.assertFalse(game.game_ended())
        game.place_marker('X', 2, 0)

        self.assertTrue(game.game_ended())
