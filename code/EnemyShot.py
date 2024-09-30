import pygame
# from code.Const import ENTITY_SPEED
# from code.Entity import Entity
#
#
# class EnemyShot(Entity):
#
#     def __init__(self, name: str, position: tuple):
#         super().__init__(name, position)
#
#     def move(self, ):
#         self.rect.centerx -= ENTITY_SPEED[self.name]
from code.Const import ENTITY_SPEED
from code.Entity import Entity
import pygame

class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Verifica se o tiro é do Enemy3 e usa o asset correto
        if name == 'Enemy3Shot':
            self.surf = pygame.image.load('./asset/Enemy3Shot.png').convert_alpha()
        else:
            # Carregar o asset padrão para outros inimigos
            self.surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()

    def move(self):
        # Movimento do tiro para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]
