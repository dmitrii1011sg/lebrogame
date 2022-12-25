import pygame

from entity.player import Player
from utils.drawing import Drawing
from settings import *


class LebroGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        self.screen_rooms = pygame.Surface(SIZE_ROOM)
        self.drawing = Drawing(self.screen, self.screen_rooms)
        self.player = Player(300)
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    exit()

            self.screen.fill(BLACK)
            self.player.movement(TEST_WALLS)
            self.drawing.draw_world(self.player.pos, TEST_WALLS)
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = LebroGame()
    game.run()
