import logging
import time
from random import randrange


class Scope:
    min_height = int(0)
    max_height = int(0)
    min_width = int(0)
    max_width = int(0)
    min_area = int(0)
    max_area = int(0)
    border = int(0)

    def __init__(self, min_height: int, max_height: int, min_width: int, max_width: int):
        self.min_height = min_height
        self.max_height = max_height
        self.min_width = min_width
        self.max_width = max_width

    def __str__(self) -> str:
        ss = f'height[{self.min_height}-{self.max_height}] width[{self.min_width}-{self.max_width}]'
        return ss

    def cal_area(self):
        self.min_area = (self.min_width + self.border) * (self.min_height + self.border)
        self.max_area = (self.max_height + self.border) * (self.max_width + self.border)


class Point:
    x = int(0)
    y = int(0)

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        ss = f'({self.y},{self.x})'
        return ss


def calc_area(top_left: Point, bottom_right: Point) -> int:
    pt = Point(abs(top_left.y - bottom_right.y), abs(top_left.x - bottom_right.x))
    area = pt.y * pt.x
    return area


class BSP:
    rooms = list()
    number_rooms = int(0)
    scope_room = Scope(0, 0, 0, 0)
    width = int(0)
    height = int(0)
    area = int(0)
    looping = int(0)

    def __init__(self, number_rooms: int, min_height: int, min_width: int):
        self.number_rooms = number_rooms

        self.scope_room.min_height = min_height
        self.scope_room.min_width = min_width
        self.scope_room.max_height = int(float(self.scope_room.min_height) * 3)
        self.scope_room.max_width = int(float(self.scope_room.min_width) * 3)
        self.scope_room.border = 2
        self.scope_room.cal_area()

        self.width = self.scope_room.min_area * self.number_rooms
        self.height = self.scope_room.min_area * self.number_rooms

        for i in range(0, self.height):
            self.rooms.append(list())

        for y in range(0, self.height):
            for x in range(0, self.width):
                self.rooms[y].append('.')

    def print(self):
        logging.info('##################')
        logging.info(f'Nombre de salles : {self.number_rooms}')
        logging.info(f'Aire             : {self.area}')
        logging.info(f'Height           : {self.height}')
        logging.info(f'Width            : {self.width}')
        logging.info(f'Scope Room       : {self.scope_room}')
        logging.info('##################')

        logging.info('~~~~~~~~~~~~~~~~~~')
        lines = '\n'
        for y in range(0, self.height - 1):
            line = str()
            for x in range(0, self.width - 1):
                line += self.rooms[y][x]
            line += '\n'
            lines += line
        logging.info(lines)
        logging.info('~~~~~~~~~~~~~~~~~~')

    def _draw_square_(self, top_left: Point, bottom_right: Point):
        self.rooms[top_left.y][top_left.x] = '*'
        self.rooms[top_left.y][bottom_right.x] = '*'
        self.rooms[bottom_right.y][bottom_right.x] = '*'
        self.rooms[bottom_right.y][top_left.x] = '*'

        for x in range(top_left.x, bottom_right.x + 1):
            # top
            if self.rooms[top_left.y][x] == '.':
                self.rooms[top_left.y][x] = '*'
            else:
                self.rooms[top_left.y][x] = '@'
            # bottom
            if self.rooms[bottom_right.y][x] == '.':
                self.rooms[bottom_right.y][x] = '*'
            else:
                self.rooms[bottom_right.y][x] = '@'

        for y in range(top_left.y, bottom_right.y + 1):
            # left
            if self.rooms[y][top_left.x] == '.':
                self.rooms[y][top_left.x] = '*'
            else:
                self.rooms[y][top_left.x] = '@'
            # right
            if self.rooms[y][bottom_right.x] == '.':
                self.rooms[y][bottom_right.x] = '*'
            else:
                self.rooms[y][bottom_right.x] = '@'

    def _verify_point_in_range_(self, pt: Point):
        if pt.y >= self.height:
            pt.y = self.height - 1
        if pt.x >= self.width:
            pt.x = self.width - 1
        return pt

    def _split_area_(self, top_left: Point, bottom_right: Point, area: int, scope: Scope, max_area: int):
        if area > max_area:
            logging.info(f'top_left: {top_left} bottom_right: {bottom_right} area: {area} max: {max_area}')

            self._draw_square_(top_left, bottom_right)

            random_height = randrange(scope.min_height, scope.max_height)
            random_width = randrange(scope.min_width, scope.max_width)

            sep_bottom_right = self._verify_point_in_range_(
                Point(top_left.y + random_height, top_left.x + random_width))

            sep_top_left = self._verify_point_in_range_(
                Point(top_left.y, top_left.x + random_width))

            area_left = calc_area(top_left, sep_bottom_right)
            area_right = calc_area(sep_top_left, bottom_right)

            logging.error(f'euh: {sep_top_left} {sep_bottom_right}')

            self.looping = self.looping + 1
            # self._split_area_(top_left, sep_bottom_right, area_left, scope, max_area)
            # self._split_area_(sep_top_left, bottom_right, area_right, scope, max_area)

    def build(self):
        start = time.time()

        top_left = Point(0, 0)
        bottom_right = Point(self.height - 1, self.width - 1)

        scope = Scope(self.scope_room.min_height, self.scope_room.max_height - 1,
                      self.scope_room.min_width, self.scope_room.max_width - 1)
        scope.border = 2
        scope.cal_area()
        self.area = calc_area(top_left, bottom_right)
        self._split_area_(top_left, bottom_right, self.area, scope, scope.max_area)

        end = time.time()
        logging.info(f'Time: {end - start} seconds')
        self.print()
        return True
