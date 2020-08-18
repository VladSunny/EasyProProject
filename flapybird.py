import pygame
from pygame.colordict import THECOLORS
from random import randint
pygame.init()
sc = pygame.display.set_mode((700, 600))
sc.fill(THECOLORS['blue'])
pygame.display.update()
FLAG = True

xb = 100
yb = 100


over_display = pygame.image.load('gameover.png')
over_display = pygame.transform.scale(over_display, (700, 600))
flapy_jump = pygame.mixer.Sound('wing.WAV')
new_point = pygame.mixer.Sound('point.WAV')
start_menu = pygame.image.load('message.png')
start_menu = pygame.transform.scale(start_menu, (700, 600))
flapybird = pygame.image.load('FLB.png')
flapybird = pygame.transform.scale(flapybird, (60, 33))#.convert()
rect_bird = flapybird.get_rect(bottomright = (100, 100))
pipe_down = pygame.image.load('pipe-green.png')
pipe_down = pygame.transform.scale(pipe_down, (100, 512))#.convert()
rect_down = pipe_down.get_rect(bottomright = (600, 300), h = 512, w = 100)
pipe_up = pygame.transform.rotate(pipe_down, 180)
rect_up = pipe_up.get_rect(bottomright = (600, 300))
game_over = False
score = 0
xp = 700
xs = xp

pip2 = False

scs = 0

menu = True



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
        if  False:
            if pip2 :
                xs -= 0.2

               # print(f"////////////////{xs}")
                sc.blit(pipe_down, rect_down)
                sc.blit(pipe_up, rect_up)
    rect_bird.y = yb
    rect_up.x = xp
    rect_down.x = xp
    rect_down.y = 300 + id
    rect_up.y = -360 + id
    sc.blit(flapybird, rect_bird)
    sc.blit(pipe_down, rect_down)
    sc.blit(pipe_up, rect_up)
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
            if rect_down.colliderect(rect_bird) or rect_up.colliderect(rect_bird):
                game_over = True
                print('stop')