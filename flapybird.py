import pygame
from pygame.colordict import THECOLORS
from random import randint
pygame.init()
sc = pygame.display.set_mode((700, 600))
sc.fill(THECOLORS['blue'])
pygame.display.update()
FLAG = True
over_display = pygame.image.load('gameover.png')
over_display = pygame.transform.scale(over_display, (700, 600))
flapy_jump = pygame.mixer.Sound('wing.WAV')
new_point = pygame.mixer.Sound('point.WAV')
start_menu = pygame.image.load('message.png')
start_menu = pygame.transform.scale(start_menu, (700, 600))
flapybird = pygame.image.load('FLB.png')
flapybird = pygame.transform.scale(flapybird, (60, 45))
pipe_down = pygame.image.load('pip.png')
pipe_down = pygame.transform.scale(pipe_down, (100, 550))
pipe_up = pygame.transform.rotate(pipe_down, 180)
game_over = False
score = 0
xp = 700
xs = xp

pip2 = False

scs = 0

menu = True

xb = 100
yb = 100

def draw_text(sc, text, x, y, size):
    font = pygame.font.SysFont('arial', size)
    text1 = font.render(f'{text}', 1, THECOLORS['white'])
    sc.blit(text1, (x, y))

#

skorost = 0.1

id = 0
while FLAG:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            FLAG = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                flapy_jump.play()
                menu = False
                yb -= 45
                skorost = 0.1
    if not game_over:
        if menu == False:
            skorost += 0.0010
            yb += skorost

            xp -= 0.2
            #print(xp, xs)

            if xp < 350:
                pip2 = True

    if not game_over:
        if menu == False:
            if pip2 :
                xs -= 0.2
               # print(f"////////////////{xs}")
                sc.blit(pipe_down, (xs, 300))
                sc.blit(pipe_up, (xs, -300))

    sc.blit(flapybird, (xb, yb))
    sc.blit(pipe_down, (xp, 300 + id))
    sc.blit(pipe_up, (xp,  -300 + id))
    if not game_over:
        if menu == True:
            sc.blit(start_menu, (0, 0))
        if menu != True:
            draw_text(sc, score, 350, 50, 50)
    else:
        sc.blit(over_display, (0, 0))
    pygame.display.update()
    sc.fill(THECOLORS['blue'])
    if not game_over:
        if menu == False:
            if 99.8 <= xp <= 100:
                score += 1
                new_point.play()
            if 99.8 <= xs <= 100:
                score += 1
                new_point.play()
            if xp <= -100:
                id = randint(-110, 110)
                xp =700
            if xs <= -100:
                xs = 700

            if xp <= xb + 60 <= xp + 100 or not 300 + id <= yb <= id + 550 + 350 or xs <= xb <= xs + 100 or 300 + id <= yb + 45 <= 300 + id + 550:
                print('stop')