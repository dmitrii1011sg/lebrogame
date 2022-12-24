import pygame

from settings import *


class LebroGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    exit()

            self.screen.fill(BLACK)
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = LebroGame()
    game.run()
