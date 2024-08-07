from typing import Any
import pygame
import time
import random
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, QUIT, KEYDOWN, K_a, K_s, K_w, K_d
)

# These will come in handy!
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

clock = pygame.time.Clock()

# Player 1 uses up and down arrow keys
class Player1(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Player1, self).__init__()
        self.surf = pygame.Surface((50, 100))          # Input an (x, y) tuple to give it a width and height
        self.surf.fill((0, 255, 0))                      # Input an (R, G, B) tuple to give it a color
        self.rect = self.surf.get_rect()
        # Right now, Player1 spawns in at (0,0). Set the x and y values of self.rect to some other numbers to change this
        self.rect.x = 0
        self.rect.y = 300

    # Updates this player's position
    def update(self, press_keys):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 600:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = 600
        if (pressed_keys[K_DOWN]):
            self.rect.y += 5
        if (pressed_keys[K_UP]):
            self.rect.y -= 5
            

# Player2 uses W and S keys
class Player2(Player1):
    def __init__(self) -> None:
        super().__init__()
        self.surf = pygame.Surface((50, 100))          # Input an (x, y) tuple to give it a width and height
        self.surf.fill((0, 255, 0))                      # Input an (R, G, B) tuple to give it a color
        self.rect = self.surf.get_rect()
        self.rect.right = 900
        self.rect.y = 300

    # Updates this player's position
    def update(self, pressed_keys):
        pressed_keys = pygame.key.get_pressed()

        if (pressed_keys[K_s]):
            self.rect.y +=5
        if (pressed_keys[K_w]):
            self.rect.y -= 5
        if self.rect.top > 600:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = 600


class Ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.surf = pygame.Surface((20, 20))          # Input an (x, y) tuple to give it a width and height
        self.surf.fill((255, 255, 255))                      # Input an (R, G, B) tuple to give it a color
        self.rect = self.surf.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.speedx = 1
        self.speedy = 1

    def update(self) -> None:
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.bottom >= 600:
            self.speedy *= -1
        if self.rect.top <= 0:
            self.speedy *= -1

   

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])     # (x, y)

# Create objects for player1, player2, and the ball here
Play1 = Player1()
play2 = Player2()

ball = Ball()

all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()

# Add those objects to all_sprites and/or players, respectively
all_sprites.add(Play1, play2, ball)
players.add(Play1, play2)

running = True
while running:
    clock.tick(500)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    # Update positions
    pressed_keys = pygame.key.get_pressed()
    for player in players:
        player.update(pressed_keys)
    if pygame.sprite.spritecollideany(ball, players):
        ball.speedx *= -1
        ball.speedy *= -1

    # Call update() on the ball here
    ball.update()

    # Render
    screen.fill((0, 0, 0))
    # Use blit() to draw each sprite on the screen here
    screen.blit(Play1.surf, Play1.rect)
    screen.blit(play2.surf, play2.rect)
    screen.blit(ball.surf, ball.rect)
    pygame.display.flip()
