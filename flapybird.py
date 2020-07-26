import pygame
from pygame.colordict import THECOLORS
pygame.init()
sc = pygame.display.set_mode((700, 600))
sc.fill(THECOLORS['blue'])
pygame.display.update()
FLAG = True
flapybird = pygame.image.load('FLB.png')
flapybird = pygame.transform.scale(flapybird, (60, 45))
pipe_down = pygame.image.load('pip.png')
pipe_down = pygame.transform.scale(pipe_down, (100, 300))
pipe_up = pygame.transform.rotate(pipe_down, 180)
score = 0

xb = 100
yb = 100

def draw_text(sc, text, x, y, size):
    font = pygame.font.SysFont('arial', size)
    text1 = font.render(f'{text}', 1, THECOLORS['white'])
    sc.blit(text1, (x, y))

skorost = 0.1


while FLAG:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            FLAG = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                yb -= 45
                skorost = 0.1

    skorost += 0.0009
    yb += skorost

    sc.blit(flapybird, (xb, yb))
    sc.blit(pipe_down, (200, 200))
    sc.blit(pipe_up, (400, 200))
    draw_text(sc, score, 450, 50, 50)
    pygame.display.update()
    sc.fill(THECOLORS['blue'])

