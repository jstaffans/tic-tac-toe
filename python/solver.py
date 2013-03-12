class Solver:
    """Checks a matrix representing a tic-tac-toe game for winning condition.
    """
    def __init__(self, matrix):
        self.matrix = matrix

    def has_won(self, symbol):
        """Checks if the given symbol has won.
           symbol -- X or O
        """
        if self._check_rows(symbol):
            return True

        if self._check_columns(symbol):
            return True

        if self._check_diagonals(symbol):
            return True

        return False

    def _check_rows(self, symbol):
        for row in self.matrix:
            if row == [symbol for j in range(3)]:
                return True
        return False

    def _check_columns(self, symbol):
        for column in range(3):
            if [row[column] for row in self.matrix] == [symbol for j in range(3)]:
                return True
        return False

    def _check_diagonals(self, symbol):
        diagonal1 = [self.matrix[i][i] for i in range(len(self.matrix))]
        diagonal2 = [self.matrix[i][len(self.matrix)-1-i] for i in range(len(self.matrix))]
        winning = [symbol for i in range(3)]

        if diagonal1 == winning or diagonal2 == winning:
            return True

        return False
