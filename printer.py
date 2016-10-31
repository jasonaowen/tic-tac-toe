# Tic Tac Toe, text UI
# Copyright (C) 2016 Jason Owen

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from game import Game, EMPTY, PLAYER_X, PLAYER_O, TIED, SIZE


def printGame(game):
    board = printBoard(game)
    state = printState(game)
    return '\n'.join([board, state])


def printBoard(game):
    return '\n'.join([
        " {} | {} | {} ",
        "---+---+---",
        " {} | {} | {} ",
        "---+---+---",
        " {} | {} | {} "
    ]).format(*[cell for row in game.cells for cell in row])


def printState(game):
    if game.winner is not None and game.winner != TIED:
        return "{} won!".format(game.winner)
    elif game.winner == TIED:
        return "Tied game!"
    else:
        return "It is {}'s turn".format(game.player)
