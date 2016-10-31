# Tic Tac Toe, main game logic
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

SPACE_EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'
SIZE = 3


class Game:
    def __init__(self, state=None, player=PLAYER_X):
        self.cells = state or [[SPACE_EMPTY] * SIZE for i in range(SIZE)]
        self.player = player

    def cell(self, x, y):
        if x in range(SIZE) and y in range(SIZE):
            return self.cells[y][x]
        else:
            raise IndexError

    def move(self, x, y):
        if self.cell(x, y) != SPACE_EMPTY:
            raise ValueError

        return Game(state=[
            [self.player if (x, y) == (col, row) else self.cell(col, row)
                for col in range(SIZE)] for row in range(SIZE)],
            player=PLAYER_O if self.player == PLAYER_X else PLAYER_X
        )
