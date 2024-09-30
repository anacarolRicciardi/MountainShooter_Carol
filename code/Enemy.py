#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


#
# class Enemy(Entity):
#     def __init__(self, name: str, position: tuple):
#         super().__init__(name, position)
#         self.shot_delay = ENTITY_SHOT_DELAY[self.name]
#
#     def move(self):
#         self.rect.centerx -= ENTITY_SPEED[self.name]
#
#     def shoot(self):
#         self.shot_delay -= 1
#         if self.shot_delay == 0:
#             self.shot_delay = ENTITY_SHOT_DELAY[self.name]
#             return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_speed = ENTITY_SPEED.get(name, 5)  # Velocidade vertical normal
        self.moving_down = False  # Controla a direção do movimento vertical

    def move(self):
        # Movimento horizontal: da direita para a esquerda
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 5)

        # Movimento vertical
        if self.moving_down:
            # Movendo para baixo com o dobro da velocidade
            self.rect.centery += self.vertical_speed * 2
            if self.rect.bottom >= WIN_HEIGHT:
                # Ao atingir a borda inferior, começar a subir com velocidade normal
                self.moving_down = False
        else:
            # Movendo para cima com velocidade normal
            self.rect.centery -= self.vertical_speed
            if self.rect.top <= 0:
                # Ao atingir a borda superior, começar a descer com o dobro da velocidade
                self.moving_down = True


    def shoot(self):
        # Reduz o atraso para o próximo tiro
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            # Reseta o atraso entre os tiros
            self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 30)
            # Cria um tiro e o retorna
            return EnemyShot(name='Enemy3Shot', position=(self.rect.centerx, self.rect.centery))