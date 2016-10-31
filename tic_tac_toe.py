# Tic Tac Toe, main game loop
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

from game import Game
from printer import printGame


def main():
    game = Game()
    print(printGame(game))

    while game.winner is None:
        validSelections = game.validSelections()
        selection = input("Move {}: ".format(validSelections + ["exit"]))
        if selection in validSelections:
            game = game.move_by_cell(selection)
        elif selection == "exit":
            return
        else:
            print("Invalid selection!")
        print(printGame(game))


if __name__ == '__main__':
    main()
