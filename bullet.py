import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):         # ai_game экземпляр класса AlienInvasion
        super().__init__()               # Получение конструктора Sprite()
        self.screen = ai_game.screen     # Получение настроек экрана
        self.settings = ai_game.settings  # Получение насттроек из файла settings
        self.color = self.settings.bullet_color # из settings получаем цвет пули
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)  # создаем пуля в координатах 0, 0 (номинальные) и размеры пули
        self.rect.midtop = ai_game.ship.rect.midtop  # получаем координаты верхней середины границы корабля и устанавливаем их для пули
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
