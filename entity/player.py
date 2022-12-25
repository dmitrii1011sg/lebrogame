import pygame
from settings import *


class Player:
    def __init__(self, pos: int, speed: int = 5) -> None:
        self.pos = pos
        self.speed = speed

    def movement(self, walls) -> None:
        keys = pygame.key.get_pressed()
        next_pos = self.pos
        if keys[pygame.K_a]:
            next_pos -= self.speed
        if keys[pygame.K_d]:
            next_pos += self.speed

        coord_rect = next_pos - (PLAYER_WIDTH//2), ROOM_HEIGHT-PLAYER_HEIGHT
        next_rect = pygame.Rect(*coord_rect, PLAYER_WIDTH, PLAYER_HEIGHT)
        if next_rect.collidelist(walls) == -1:
            self.pos = next_pos


