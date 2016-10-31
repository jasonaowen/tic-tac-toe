# Tic Tac Toe, unit tests
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


class TestGame(unittest.TestCase):
    def test_can_create_game(self):
        game = Game()
        self.assertIsNotNone(game)

    def test_new_game_has_empty_board(self):
        game = Game()
        for (x, y) in [(x, y) for x in range(SIZE) for y in range(SIZE)]:
            self.assertEqual(EMPTY, game.cell(x, y))

    def test_first_player_is_x(self):
        game = Game()
        game = game.move(0, 0)
        self.assertEqual(PLAYER_X, game.cell(0, 0))

    def test_second_player_is_o(self):
        game = Game().move(0, 0).move(0, 1)
        self.assertEqual(PLAYER_O, game.cell(0, 1))

    def test_third_player_is_x_again(self):
        game = Game().move(0, 0).move(0, 1).move(0, 2)
        self.assertEqual(PLAYER_X, game.cell(0, 2))

    def test_cannot_move_in_taken_position(self):
        with self.assertRaises(ValueError):
            Game().move(0, 0).move(0, 0)

    def test_can_win_game_vertically(self):
        game = (Game().move(0, 0)
                      .move(2, 2)
                      .move(0, 1)
                      .move(2, 1)
                      .move(0, 2))
        self.assertEqual(PLAYER_X, game.winner)
        with self.assertRaises(ValueError):
            game.move(1, 1)

    def test_can_win_game_horizontally(self):
        game = (Game().move(0, 0)
                      .move(2, 2)
                      .move(1, 0)
                      .move(1, 2)
                      .move(2, 0))
        self.assertEqual(PLAYER_X, game.winner)
        with self.assertRaises(ValueError):
            game.move(1, 1)

    def test_can_win_game_diagonally(self):
        game = (Game().move(0, 2)
                      .move(0, 0)
                      .move(1, 0)
                      .move(1, 1)
                      .move(0, 1)
                      .move(2, 2))
        self.assertEqual(PLAYER_O, game.winner)
        with self.assertRaises(ValueError):
            game.move(2, 1)

    def test_can_tie_game(self):
        game = (Game().move(0, 0)   # X
                      .move(0, 1)   # O
                      .move(0, 2)   # X
                      .move(1, 1)   # O
                      .move(1, 0)   # X
                      .move(1, 2)   # O
                      .move(2, 1)   # X
                      .move(2, 0)   # O
                      .move(2, 2))  # X
        self.assertEqual(TIED, game.winner)
