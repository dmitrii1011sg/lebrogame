import pygame

from entity.player import Player
from service.map_service import MapService
from utils.drawing import Drawing
from settings import *


class LebroGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        self.screen_rooms = pygame.Surface(SIZE_ROOM)
        self.map_service = MapService()
        self.map_service.load_map_local(1)
        self.drawing = Drawing(self.screen, self.screen_rooms)
        self.player = Player(500)
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    exit()

            self.screen.fill(BLACK)
            self.player.movement(self.map_service.walls_rect)
            self.drawing.draw_world(self.player.pos, self.map_service.background_walls, self.map_service.walls_rect)
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = LebroGame()
    game.run()
