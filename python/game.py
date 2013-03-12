from solver import *

class IllegalActionException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)

EMPTY_SLOT = ' '

def create_empty_game_matrix():
    return [[EMPTY_SLOT for i in range(3)] for j in range(3)]

class Game:
    """This class contains the main game logic: setting markers, enforcing turns and
       checking for winning conditions.
    """

    MARKERS = ['X', 'O']

    def __init__(self):
        self.matrix = create_empty_game_matrix()
        self.next_in_turn = self.MARKERS[0]

    def place_marker(self, symbol, x, y):
        if symbol not in self.MARKERS:
            raise IllegalActionException('Invalid symbol.')

        if symbol != self.next_in_turn:
            raise IllegalActionException('Not your turn.')

        if self._marker_out_of_bounds(x, y):
            raise IllegalActionException('Marker out of bounds.')

        if self.matrix[y][x] != EMPTY_SLOT:
            raise IllegalActionException('Slot already occupied.')

        self.matrix[y][x] = symbol
        self._next_turn()

    def _marker_out_of_bounds(self, x, y):
        return x < 0 or x > 2 or y < 0 or y > 2

    def _next_turn(self):
        if self.next_in_turn == self.MARKERS[0]:
            self.next_in_turn = self.MARKERS[1]
        else:
            self.next_in_turn = self.MARKERS[0]

    def game_ended(self):
        solver = Solver(self.matrix)
        return solver.has_won(self.MARKERS[0]) or solver.has_won(self.MARKERS[1])

    def get_matrix(self):
        return self.matrix

