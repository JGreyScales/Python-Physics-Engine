import pygame
import random
  
# GLOBAL VARIABLES
WIDTH = 500
HEIGHT = 500
  
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(128,128,128)
        self.image.set_colorkey(255,255,255)
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()
  
  
pygame.init()

  
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
  
all_sprites_list = pygame.sprite.Group()
  
object_ = Sprite((0, 0, 0), 20, 30)
object_.rect.x = 200
object_.rect.y = 300
  
all_sprites_list.add(object_)
  
looping = True
clock = pygame.time.Clock()
  
while looping:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looping = False
  
    all_sprites_list.update()
    screen.fill(128,128,128)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
  
pygame.quit()