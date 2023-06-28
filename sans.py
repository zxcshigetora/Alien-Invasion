import pygame
from pygame.sprite import Sprite


class Sans(Sprite):

    def __init__(self, sansik):
        super().__init__()
        self.screen = sansik.screen                                  # Получение самого экрана
        self.settings_of_screen = sansik.screen.get_rect()           # Получение размеров экрана
        self.image = pygame.image.load('images/sans.bmp')             # Загрузка изображения
        self.rect = self.image.get_rect()                 # Получение размеров изображения self.sans
        self.screen_location = self.settings_of_screen.midtop        # Координаты верхней серединной точки экрана
        self.location = self.rect.midtop                 # Координаты верхней серединной точки санса
        self.rect.x = self.rect.width                         # Получение ширины санса
        self.rect.y = self.rect.height                        # Получение высоты санса
        self.x = float(self.rect.x)
        self.settings = sansik.settings

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
