import logging
import time
from random import randrange


class Cell:
    x = int(0)
    y = int(0)

    def __init__(self, y: int, x: int):
        self.y = int(y)
        self.x = int(x)

    def __str__(self) -> str:
        ss = f'({self.y},{self.x})'
        return ss


def get_wall_cell(brut_cell: Cell, brut_neighbour: Cell) -> Cell or None:
    wall = Cell(brut_cell.y, brut_cell.x)

    if brut_cell.y != brut_neighbour.y:
        if brut_cell.y > brut_neighbour.y:
            wall.y = wall.y - 1
        else:
            wall.y = wall.y + 1
    elif brut_cell.x != brut_neighbour.x:
        if brut_cell.x > brut_neighbour.x:
            wall.x = wall.x - 1
        else:
            wall.x = wall.x + 1
    else:
        return None

    return wall


class Grid:

    cell_usless = '.'
    cell_wall_h = '_'
    cell_wall_v = '|'
    cell_coridor = ' '
    width = 10
    height = 10

    def __init__(self, width: int = 10, height: int = 10):
        self.width = width
        self.height = height
        self.grid = []

    def print(self):
        line_nb = False
        lines = str()
        for y in range(0, self.height * 2 + 1):
            line = str()
            if not line_nb:
                for x in range(0, self.width * 2, 2):
                    line += self.grid[y][x]
                    line += ' '
                    line += self.grid[y][x + 1]
            else:
                for x in range(0, self.width * 2 + 1):
                    line += str(self.grid[y][x])
            line_nb = False if line_nb else True
            lines += f'{line}\n'
        logging.info(
            f'height:{self.height} * width:{self.width}'
            f'\n{lines}')

    def axe_y_number(self, y: int) -> int:
        if y >= self.height:
            y = y - 1
        elif y < 0:
            y = 0
        return y * 2 + 1

    def axe_x_number(self, x: int) -> int:
        if x >= self.width:
            x = x - 1
        elif x < 0:
            x = 0
        return x * 2 + 1

    def get_number(self, y: int, x: int) -> int:
        return self.grid[self.axe_y_number(y)][self.axe_x_number(x)]

    def get_wall(self, y: int, x: int) -> str:
        if y % 2 == 0:
            return ''
        else:
            return self.grid[y][x]

    def get_cell_neighbour(self, cell: Cell) -> Cell or None:
        neighbour = Cell(cell.y, cell.x)

        # Une direction (gauche, droite, haut, bas)
        direction = randrange(1, 5)
        if direction == 1:
            neighbour.x = neighbour.x - 1
        elif direction == 2:
            neighbour.x = neighbour.x + 1
        elif direction == 3:
            neighbour.y = neighbour.y - 1
        elif direction == 4:
            neighbour.y = neighbour.y + 1

        # Hors map
        if neighbour.y >= self.height or neighbour.y < 0:
            return None
        if neighbour.x >= self.width or neighbour.x < 0:
            return None

        return neighbour

    def update_case_number__(self, new_val: int, old_val: int):
        line_nb = False
        for y in range(self.height * 2):
            if line_nb:
                for x in range(1, self.width * 2 + 1, 2):
                    if self.grid[y][x] == old_val:
                        self.grid[y][x] = new_val
            line_nb = False if line_nb else True

    def is_unique_number_case(self):
        first_val = self.grid[1][1]
        line_nb = False
        for y in range(self.height * 2):
            if line_nb:
                for x in range(1, self.width * 2 + 1, 2):
                    if self.grid[y][x] != first_val:
                        return False
            line_nb = False if line_nb else True
        return True

    def initialize(self):
        self.grid = [[] for _ in range(self.height * 2 + 1)]

        val = int(0)
        swap = False
        for line in self.grid:
            if not swap:
                for i in range(self.width):
                    line += self.cell_usless
                    line += self.cell_wall_h
            else:
                for i in range(self.width):
                    line += self.cell_wall_v
                    line += self.cell_usless
                    line[i * 2 + 1] = val
                    val = val + 1
                    if i == self.width - 1:
                        line += self.cell_wall_v
            swap = False if swap else True

    def build(self):
        start = time.time()
        max_iterate = self.height * self.width * 10
        loop = 0
        # first cell : self.grid[1][1]
        # last cell  : self.grid[self.height * 2 - 1][self.width * 2 - 1]:
        while not self.is_unique_number_case():
            if loop >= max_iterate:
                break
            loop = loop + 1

            y = randrange(0, self.height)
            x = randrange(0, self.width)
            cell = Cell(y, x)
            neighbour = self.get_cell_neighbour(cell)
            if not neighbour:
                continue

            brut_cell = Cell(self.axe_y_number(cell.y), self.axe_x_number(cell.x))
            brut_neighbour = Cell(self.axe_y_number(neighbour.y), self.axe_x_number(neighbour.x))

            val = self.get_number(cell.y, cell.x)
            val_neighbour = self.get_number(neighbour.y, neighbour.x)
            if val != val_neighbour:
                wall = get_wall_cell(brut_cell, brut_neighbour)
                self.grid[wall.y][wall.x] = self.cell_coridor
                self.update_case_number__(val, val_neighbour)

        end = time.time()
        self.print()
        if loop == max_iterate:
            logging.info('ending forced')
        else:
            logging.info(f'Iterate:{loop} / {max_iterate}')
            logging.info(f'Time:{end - start} seconds')
