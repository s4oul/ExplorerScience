import argparse
import logging

from grid import Grid
from bsp import BSP


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--type',
        type=str,
        choices=['labyrinthe', 'salles'],
        default='labyrinthe',
        help='an integer for the accumulator'
    )
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
    parser.add_argument(
        '--number_rooms',
        type=int,
        default=10,
        help='an integer for the accumulator'
    )
    options = parser.parse_args()

    if options.type == 'labyrinthe':
        logging.info('Génération d un labyrinthe')
        grid = Grid(options.width, options.height)
        grid.initialize()
        logging.info('Grille de départ')
        grid.print()
        logging.info('Labyrinthe parfaite')
        grid.build()
    elif options.type == 'salles':
        logging.info('Génération d un monde de salles')
        bsp = BSP(options.number_rooms, options.height, options.width)
        logging.info('Building BSP')
        bsp.build()
        #bsp.print()

