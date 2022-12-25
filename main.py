import pygame

from entity.player import Player
from utils.drawing import Drawing
from settings import *


class LebroGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        self.screen_rooms = pygame.Surface((WIDTH, 400))
        self.player = Player(50)
        self.drawing = Drawing(self.screen, self.screen_rooms)
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    exit()

            self.screen.fill(BLACK)
            self.player.movement()
            self.drawing.draw_player(self.player.point)
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = LebroGame()
    game.run()
