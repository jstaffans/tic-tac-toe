class Printer:

    def __init__(self, game):
        self.game = game

    def print_game(self):
        matrix = self.game.get_matrix()
        self._print_horizontal_line()
        for row in matrix:
            self._print_cells(row)
            self._print_horizontal_line()

    def _print_horizontal_line(self):
        print '+---+---+---+'

    def _print_cells(self, row):
        print '| %s | %s | %s |' % (row[0], row[1], row[2])
