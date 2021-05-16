import argparse
import logging

from grid import Grid


if __name__ == '__main__':
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--width',
        type=int,
        default=10,
        help='an integer for the accumulator'
    )
    parser.add_argument(
        '--height',
        type=int,
        default=10,
        help='an integer for the accumulator'
    )
    options = parser.parse_args()

    grid = Grid(options.width, options.height)
    grid.initialize()
    logging.info('Grille de départ')
    grid.print()
    logging.info('Labyrinthe parfaite')
    grid.build()
