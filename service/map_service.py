import json

import pygame

from settings import *


class MapService:
    def __init__(self) -> None:
        self.walls = list()
        self.background_walls = list()
        self.walls_rect = list()

    def load_map_local(self, number_map):
        file = open(f'assets/maps/room{number_map}.json')
        data = json.load(file)
        file.close()
        self.walls = data['walls']
        self.background_walls = data['background_walls']
        self.walls_rect = [pygame.Rect(ind*TILE, 0, TILE, ROOM_HEIGHT) for ind, i in enumerate(self.walls) if i == 1]
        print(self.walls_rect )
