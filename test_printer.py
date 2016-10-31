# Tic Tac Toe, text UI unit tests
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

import unittest

from game import Game, EMPTY, PLAYER_X, PLAYER_O, TIED, SIZE
from printer import printGame


class TestPrinter(unittest.TestCase):
    def test_can_create_game(self):
        game = Game()
        expected = '\n'.join([
                "   |   |   ",
                "---+---+---",
                "   |   |   ",
                "---+---+---",
                "   |   |   ",
                "It is X's turn"])
        self.assertEqual(expected, printGame(game))

    def test_one_move(self):
        game = Game().move_by_point(0, 0)
        expected = '\n'.join([
                " X |   |   ",
                "---+---+---",
                "   |   |   ",
                "---+---+---",
                "   |   |   ",
                "It is O's turn"])
        self.assertEqual(expected, printGame(game))

    def test_two_moves(self):
        game = Game().move_by_point(0, 0).move_by_point(1, 0)
        expected = '\n'.join([
                " X | O |   ",
                "---+---+---",
                "   |   |   ",
                "---+---+---",
                "   |   |   ",
                "It is X's turn"])
        self.assertEqual(expected, printGame(game))

    def test_tied_game(self):
        game = (Game().move_by_point(0, 0)   # X
                      .move_by_point(0, 1)   # O
                      .move_by_point(0, 2)   # X
                      .move_by_point(1, 1)   # O
                      .move_by_point(1, 0)   # X
                      .move_by_point(1, 2)   # O
                      .move_by_point(2, 1)   # X
                      .move_by_point(2, 0)   # O
                      .move_by_point(2, 2))  # X
        expected = '\n'.join([
                " X | O | X ",
                "---+---+---",
                " X | O | O ",
                "---+---+---",
                " O | X | X ",
                "Tied game!"])
        self.assertEqual(TIED, game.winner)

    def test_x_wins(self):
        game = (Game().move_by_point(0, 0)   # X
                      .move_by_point(2, 2)   # O
                      .move_by_point(0, 1)   # X
                      .move_by_point(2, 1)   # O
                      .move_by_point(0, 2))  # X
        expected = '\n'.join([
                " X | X | X ",
                "---+---+---",
                "   |   |   ",
                "---+---+---",
                "   | O | O ",
                "X won!"])
        self.assertEqual(PLAYER_X, game.winner)

    def test_o_wins(self):
        game = (Game().move_by_point(0, 0)   # X
                      .move_by_point(2, 2)   # O
                      .move_by_point(1, 1)   # X
                      .move_by_point(2, 1)   # O
                      .move_by_point(0, 2)   # X
                      .move_by_point(2, 0))  # O
        expected = '\n'.join([
                " X |   | X ",
                "---+---+---",
                "   | X |   ",
                "---+---+---",
                " O | O | O ",
                "O won!"])
        self.assertEqual(PLAYER_O, game.winner)


if __name__ == '__main__':
    unittest.main()
