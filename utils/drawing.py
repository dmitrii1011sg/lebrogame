import pygame
from settings import *


class Drawing:
    def __init__(self, screen, screen_rooms) -> None:
        self.screen = screen
        self.screen_rooms = screen_rooms

    # def draw_world(self, player_pos, walls):
    #     self.screen_rooms.fill(BLACK)
    #     [pygame.draw.rect(self.screen_rooms, WHITE, i) for i in walls]
    #     player_rect = pygame.Rect(
    #         player_pos - (PLAYER_WIDTH // 2), ROOM_HEIGHT - PLAYER_HEIGHT,
    #         PLAYER_WIDTH, PLAYER_HEIGHT
    #     )
    #     pygame.draw.rect(self.screen_rooms, RED, player_rect)
    #     self.screen.blit(self.screen_rooms, (0, TOP_MARGIN))

    def draw_world(self, player_pos, background_walls, walls):
        self.screen_rooms.fill(BLACK)
        camera_rect = pygame.Rect(player_pos-HALF_WIDTH, 0, WIDTH, HEIGHT)
        visible_walls = list()
        diff = HALF_WIDTH - player_pos
        for wall in walls:
            if camera_rect.colliderect(wall):
                visible_walls.append(wall)
                pygame.draw.rect(self.screen_rooms, WHITE, pygame.Rect(wall.x+diff, wall.y, TILE, ROOM_HEIGHT))
        player_rect = pygame.Rect(
            HALF_WIDTH - (PLAYER_WIDTH // 2), ROOM_HEIGHT - PLAYER_HEIGHT,
            PLAYER_WIDTH, PLAYER_HEIGHT
        )
        pygame.draw.rect(self.screen_rooms, RED, player_rect)
        self.screen.blit(self.screen_rooms, (0, TOP_MARGIN))

