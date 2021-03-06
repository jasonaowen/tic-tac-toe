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

EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'
TIED = '-'
SIZE = 3
COLUMN_NAMES = ['A', 'B', 'C']
ROW_NAMES = ['1', '2', '3']


class Game:
    def __init__(self, state=None, player=PLAYER_X):
        self.cells = state or [[EMPTY] * SIZE for i in range(SIZE)]
        self.player = player
        self.winner = self.calculate_winner()

    def cell(self, x, y):
        if x in range(SIZE) and y in range(SIZE):
            return self.cells[y][x]
        else:
            raise IndexError

    def move_by_cell(self, cell_name):
        if len(cell_name) != 2:
            raise ValueError
        x = COLUMN_NAMES.index(cell_name[0])
        y = ROW_NAMES.index(cell_name[1])
        return self.move_by_point(x, y)

    def move_by_point(self, x, y):
        if self.cell(x, y) != EMPTY:
            raise ValueError
        if self.winner is not None:
            raise ValueError

        return Game(state=[
            [self.player if (x, y) == (col, row) else self.cell(col, row)
                for col in range(SIZE)] for row in range(SIZE)],
            player=PLAYER_O if self.player == PLAYER_X else PLAYER_X
        )

    def calculate_winner(self):
        for potentially_winning_sequence in self.sequences():
            cell_set = set(potentially_winning_sequence)
            if len(cell_set) == 1 and EMPTY not in cell_set:
                return cell_set.pop()
        if EMPTY not in set([cell for row in self.cells for cell in row]):
            return TIED
        return None

    def sequences(self):
        return ([[self.cell(x, y) for x in range(SIZE)] for y in range(SIZE)] +
                [[self.cell(x, y) for y in range(SIZE)] for x in range(SIZE)] +
                [[self.cell(i, i) for i in range(SIZE)]] +
                [[self.cell(i, SIZE-i-1) for i in range(SIZE)]]
                )

    def validSelections(self):
        return [
            COLUMN_NAMES[x] + ROW_NAMES[y]
            for x in range(SIZE)
            for y in range(SIZE)
            if self.cell(x, y) == EMPTY
        ]
