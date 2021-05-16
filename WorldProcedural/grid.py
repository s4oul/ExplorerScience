import time
from random import randrange


grid_wall_h = '|'
grid_wall_v = '_'


class Cell:
    x = int(0)
    y = int(0)

    def __init__(self, y: int, x: int):
        self.y = int(y)
        self.x = int(x)

    def __str__(self) -> str:
        ss = f'({self.y},{self.x})'
        return ss


class Grid:

    def __init__(self, width: int = 10, height: int = 10):
        self.width = width
        self.height = height
        self.grid = []

    def print(self):
        line_nb = False
        for y in range(0, self.height * 2 + 1):
            line = str()
            if not line_nb:
                for x in range(0, self.width * 2, 2):
                    line += self.grid[y][x]
                    line += ' '
                    line += self.grid[y][x + 1]
            else:
                for x in range(0, self.width * 2 + 1):
                    if type(self.grid[y][x]) is int and self.grid[y][x] < 10:
                        line += ' '
                    line += str(self.grid[y][x])
            line_nb = False if line_nb else True
            print(line)

    def initialize(self):
        self.grid = [[] for i in range(self.height * 2 + 1)]

        val = int(0)
        swap = False
        for line in self.grid:
            if not swap:
                for i in range(self.width):
                    line += '.'
                    line += '_'
            else:
                for i in range(self.width):
                    line += '|'
                    line += '0'
                    line[i * 2 + 1] = val
                    val = val + 1
                    if i == self.width - 1:
                        line += '|'
            swap = False if swap else True

    def __axe_y_number__(self, y: int) -> int:
        if y >= self.height:
            y = self.height - 1
        return y * 2 + 1

    def __axe_x_number__(self, x: int) -> int:
        return x * 2 + 1

    def __get_number(self, y: int, x: int) -> int:
        return self.grid[self.__axe_y_number__(y)][self.__axe_x_number__(x)]

    def __get_wall(self, y: int, x: int) -> str:
        if y % 2 == 0:
            return ''
        else:
            return self.grid[y][x]

    def __get_neighbour__(self, cell: Cell) -> Cell or None:
        neighbour = Cell(cell.y, cell.x)
        direction = randrange(1, 5)
        if direction == 1:
            # left
            neighbour.x = neighbour.x - 1
            if neighbour.x < 0:
                return None
        elif direction == 2:
            # right
            neighbour.x = neighbour.x + 1
            if neighbour.x >= self.width:
                return None
        elif direction == 3:
            # top
            neighbour.y = neighbour.y - 1
            if neighbour.y < 0:
                return None
        elif direction == 4:
            # bottom
            neighbour.y = neighbour.y + 1
            if neighbour.y >= self.height:
                return None
        return neighbour

    def __get_wall_cell__(self, brut_cell: Cell, brut_neighbour: Cell) -> Cell:
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

    def __update_case_number__(self, new_val: int, old_val: int):
        line_nb = False
        for y in range(self.height * 2):
            if line_nb:
                for x in range(1, self.width * 2 + 1, 2):
                    if self.grid[y][x] == old_val:
                        self.grid[y][x] = new_val
            line_nb = False if line_nb else True

    def __is_unique_number_case__(self):
        first_val = self.grid[1][1]
        line_nb = False
        for y in range(self.height * 2):
            if line_nb:
                for x in range(1, self.width * 2 + 1, 2):
                    if self.grid[y][x] != first_val:
                        return False
            line_nb = False if line_nb else True
        return True

    def build(self):
        start = time.time()
        max_iterate = self.height * self.width * 10000
        loop = 0
        # while self.grid[1][1] != self.grid[self.height * 2 - 1][self.width * 2 - 1]:
        while not self.__is_unique_number_case__():
            if loop >= max_iterate:
                break
            loop = loop + 1

            y = randrange(self.height)
            x = randrange(self.width)
            cell = Cell(y, x)
            neighbour = self.__get_neighbour__(cell)
            if not neighbour:
                continue

            brut_cell = Cell(self.__axe_y_number__(cell.y), self.__axe_y_number__(cell.x))
            brut_neighbour = Cell(self.__axe_y_number__(neighbour.y), self.__axe_y_number__(neighbour.x))

            val = self.__get_number(cell.y, cell.x)
            val_neighbour = self.__get_number(neighbour.y, neighbour.x)
            if val != val_neighbour:
                wall = self.__get_wall_cell__(brut_cell, brut_neighbour)
                self.grid[wall.y][wall.x] = ' '
                self.__update_case_number__(val, val_neighbour)

        end = time.time()
        self.print()
        if loop == max_iterate:
            print(f'ending forced')
        else:
            print(f'Iterate:{loop} / {max_iterate}')
            print(f'Time:{end - start} seconds')
