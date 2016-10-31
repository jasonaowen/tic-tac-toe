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

from game import Game, SPACE_EMPTY, PLAYER_X, PLAYER_O, SIZE
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
        game = Game().move(0, 0)
        expected = '\n'.join([
                " X |   |   ",
                "---+---+---",
                "   |   |   ",
                "---+---+---",
                "   |   |   ",
                "It is O's turn"])
        self.assertEqual(expected, printGame(game))

    def test_two_moves(self):
        game = Game().move(0, 0).move(1, 0)
        expected = '\n'.join([
                " X | O |   ",
                "---+---+---",
                "   |   |   ",
                "---+---+---",
                "   |   |   ",
                "It is X's turn"])
        self.assertEqual(expected, printGame(game))
