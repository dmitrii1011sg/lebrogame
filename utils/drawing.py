import pygame
from settings import *


class Drawing:
    def __init__(self, screen, screen_rooms) -> None:
        self.screen = screen
        self.screen_rooms = screen_rooms

    def draw_player(self, point: int):
        self.screen_rooms.fill(BLACK)
        rect_player = pygame.Rect(point-30, 0, 60, 100)
        pygame.draw.rect(self.screen_rooms, WHITE, rect_player)
        self.screen.blit(self.screen_rooms, (0, TOP_MARGIN))
