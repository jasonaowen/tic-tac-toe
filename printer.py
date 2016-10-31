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

from game import (Game,
                  PLAYER_X, PLAYER_O,
                  EMPTY, TIED,
                  SIZE,
                  COLUMN_NAMES, ROW_NAMES)

ROW_DIVIDER = "   ---+---+---"


def printGame(game):
    board = printBoard(game)
    state = printState(game)
    return '\n'.join([board, state])


def printBoard(game):
    return '\n'.join([
        printHeader(COLUMN_NAMES),
        printRow(ROW_NAMES[0], game.cells[0]),
        ROW_DIVIDER,
        printRow(ROW_NAMES[1], game.cells[1]),
        ROW_DIVIDER,
        printRow(ROW_NAMES[2], game.cells[2]),
    ])


def printHeader(column_names):
    return "    {}   {}   {} ".format(*column_names)

def printRow(rowName, cells):
    return " {}  {} | {} | {} ".format(*([rowName] + cells))


def printState(game):
    if game.winner is not None and game.winner != TIED:
        return "{} won!".format(game.winner)
    elif game.winner == TIED:
        return "Tied game!"
    else:
        return "It is {}'s turn".format(game.player)
