def has_won(symbol, matrix):
    if check_rows(symbol, matrix):
        return True

    if check_columns(symbol, matrix):
        return True

    if check_diagonals(symbol, matrix):
        return True

    return False

def check_rows(symbol, matrix):
    for row in matrix:
        if row == [symbol for j in range(3)]:
            return True
    return False

def check_columns(symbol, matrix):
    for column in range(3):
        if [row[column] for row in matrix] == [symbol for j in range(3)]:
            return True
    return False

def check_diagonals(symbol, matrix):
    diagonal1 = [matrix[i][i] for i in range(len(matrix))]
    diagonal2 = [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]
    winning = [symbol for i in range(3)]

    if diagonal1 == winning or diagonal2 == winning:
        return True
    return False
