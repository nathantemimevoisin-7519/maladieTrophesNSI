import pygame
LARGEUR =100
HAUTEUR =100

class Vaisseau(pygame.sprite.Sprite):
    score =0
    def __init__(self,x,y):
        self.image = pygame.image.load("vaisseau.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

pygame.init()
ecran = pygame.display.set_mode((LARGEUR,HAUTEUR))
lv = pygame.sprite.Group()
v1 = Vaisseau(10,10)
lv.add(v1)
