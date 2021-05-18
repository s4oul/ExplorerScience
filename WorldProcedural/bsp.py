import logging
import time
from random import randrange


class BSP:

    rooms = list()
    number_rooms = int(10)
    min_height = int(10)
    min_width = int(10)
    width = int(10)
    height = int(10)
    total = int(10)

    def __init__(self, number_rooms: int, min_height: int, min_width: int):
        self.number_rooms = number_rooms
        self.min_height = min_height
        self.min_width = min_width

        self.width = self.min_width * self.number_rooms + 2 * self.number_rooms
        self.height = self.min_height * self.number_rooms + 2 * self.number_rooms

        for i in range(0, self.height):
            self.rooms.append(list())

        for y in range(0, self.height):
            for x in range(0, self.width):
                self.rooms[y].append('.')

    def print(self):
        logging.info('##################')
        logging.info(f'Nombre de salles : {self.number_rooms}')
        logging.info(f'Aire             : {self.total}')
        logging.info(f'Height           : [{self.height}]')
        logging.info(f'Width            : {self.width}')
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

    def build(self):
        start = time.time()

        self.total = self.height * self.width

        for i in range(0, self.number_rooms):
            pass

        end = time.time()
        logging.info(f'Time: {end - start} seconds')
        return True
