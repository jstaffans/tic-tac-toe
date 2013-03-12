from game import *
from printer import *

game = Game()
printer = Printer(game)

print 'X starts, e.g. "X 2 2" to place a marker in the middle of the matrix.'

printer.print_game()

while True:
    cmd = raw_input('tic-tac-toe> ')

    if cmd == 'Q':
        break

    args = cmd.split(' ')

    if len(args) != 3:
        print 'Usage: <X|O> <x> <y>, where x,y = [1,3]. Q to quit.'
        continue

    try:
        game.place_marker(args[0], int(args[1])-1, int(args[2])-1)
    except Exception as e:
        print e.message

    printer.print_game()

    if game.game_ended():
        print 'You win!'
        break
