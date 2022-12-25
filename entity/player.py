import pygame


class Player:
    def __init__(self, point: int, speed: int = 2) -> None:
        self.point = point
        self.speed = speed

    def movement(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.point -= self.speed
        if keys[pygame.K_d]:
            self.point += self.speed
