import pygame

from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_game):                          # ai_game экземпляр класса AlienInvasion
        super().__init__()
        self.screen = ai_game.screen                      # Получение настроек экрана
        self.screen_rect = ai_game.screen.get_rect()      # Атрибут с размерами поверхности экрана
        self.image = pygame.image.load('images/chara.bmp') # Создаем атрибут класса с картинкой, подгружаем ее
        self.rect = self.image.get_rect()                 # Создаем прямоугольник с размерами картинки
        self.rect.midbottom = self.screen_rect.midbottom  # Координаты нижней поверхности, по середине.
        self.speed = ai_game.settings.ship_speed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False                         # Флаг нажатой кнопки
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
