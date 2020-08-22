import pygame
from pygame.colordict import THECOLORS
from random import randint
import sqlite3
conn = sqlite3.connect('bd.sqlite')

cur = conn.cursor()

cur.execute("""select name, score from Score;""")


name, gl_score = cur.fetchone()

gl_score = int(gl_score)

pygame.init()
sc = pygame.display.set_mode((700, 600))
sc.fill(THECOLORS['blue'])
pygame.display.update()
FLAG = True

xc = 0
monet = False
yc = 0

xb = 100
yb = 100


over_display = pygame.image.load('gameover.png')
over_display = pygame.transform.scale(over_display, (700, 600))
flapy_jump = pygame.mixer.Sound('wing.WAV')
hat1 = pygame.image.load('hat_1.png')
hat2 = pygame.image.load('hat_2.png')
hat3 = pygame.image.load('hat_3.png')
hat1 = pygame.transform.scale(hat1, (40, 40))
hat2 = pygame.transform.scale(hat2, (40, 40))
hat3 = pygame.transform.scale(hat3, (40, 40))
new_point = pygame.mixer.Sound('point.WAV')
start_menu = pygame.image.load('message.png')
start_menu = pygame.transform.scale(start_menu, (700, 600))
flapybird = pygame.image.load('FLB.png')
flapybird = pygame.transform.scale(flapybird, (60, 33))#.convert()
rect_bird = flapybird.get_rect(bottomright = (100, 100))
pipe_down = pygame.image.load('pipe-green.png')
pipe_down = pygame.transform.scale(pipe_down, (100, 512)).convert()
rect_down = pipe_down.get_rect(bottomright = (600, 300), h = 512, w = 100)
pipe_up = pygame.transform.rotate(pipe_down, 180)
rect_up = pipe_up.get_rect(bottomright = (600, 300))
game_over = False
score = 0
xp = 700
xs = xp

hat_1 = False
hat_2 = False
hat_3 = False

pip2 = False

scs = 0

menu = True

mone = 0

menu = False


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
            if i.key == pygame.K_SPACE and game_over == True:
                xp = 700
                xs = 700
                yb = 300
                pip2 = False
                game_over = False
            elif i.key == pygame.K_SPACE:
                flapy_jump.play()
                menu = False
                yb -= 45
                skorost = 0.1
            if i.key == pygame.K_e:
                if menu == False:
                    menu = True
                else:
                    menu = False
            if i.key == pygame.K_1:
                if menu == True:
                    print('aaaaa')
                    if mone >= 3:
                        mone -= 3
                        hat_1 = True
                        hat_2 = False
                        hat_3 = False
                        print('aaaaaa')
            if i.key == pygame.K_2:
                if menu == True:
                    if mone >= 5:
                        mone -= 5
                        hat_2 = True
                        hat_1 = False
                        hat_3 = False
            if i.key == pygame.K_3:
                if menu == True:
                    if mone >= 7:
                        hat_3 = True
                        hat_2 = False
                        hat_1 = False
                        mone -= 7

    if not game_over:
        if menu == False:
            skorost += 0.0010
            yb += skorost

            xp -= 0.2
            #print(xp, xs)

            if xp < 350:
                pip2 = True

    if not game_over and not menu:
        if pip2 :
            xs -= 0.2
            rect_up.x = xs
            rect_down.x = xs
           # print(f"////////////////{xs}")
            sc.blit(pipe_down, rect_down)
            sc.blit(pipe_up, rect_up)
            if rect_down.colliderect(rect_bird) or rect_up.colliderect(rect_bird):
                game_over = True
                print('stop')
    rect_bird.y = yb
    rect_up.x = xp
    rect_down.x = xp
    rect_down.y = 300 + id
    rect_up.y = -360 + id
    if menu == True:
        hat1 = pygame.transform.scale(hat1, (100, 100))
        hat2 = pygame.transform.scale(hat2, (100, 100))
        hat3 = pygame.transform.scale(hat3, (100, 100))
        sc.blit(hat1, (100, 500))
        sc.blit(hat2, (200, 500))
        sc.blit(hat3, (300, 500))
        draw_text(sc, '30', 100, 450, 30)
        draw_text(sc, '50', 200, 450, 30)
        draw_text(sc, '70', 300, 450, 30)

    if monet == False:
        monet = True
        xc = 70
        yc = randint(100, 500)
    if monet == True:
        pygame.draw.circle(sc, THECOLORS['yellow'], (xc, yc), 10)
    sc.blit(flapybird, rect_bird)
    hat1 = pygame.transform.scale(hat1, (30, 30))
    hat2 = pygame.transform.scale(hat2, (30, 30))
    hat3 = pygame.transform.scale(hat3, (30, 30))
    if hat_1 == True:
        sc.blit(hat1, (50, yb - 15))
    if hat_2 == True:
        sc.blit(hat2, (50, yb - 15))
    if hat_3 == True:
        sc.blit(hat3, (50, yb - 15))
    sc.blit(pipe_down, rect_down)
    sc.blit(pipe_up, rect_up)
    draw_text(sc, str(gl_score), 400, 50, 30)
    draw_text(sc, str(mone), 200, 50, 35)
    #print(gl_score)
    if not game_over and menu != True:
        if menu == True:
            sc.blit(start_menu, (0, 0))
        if menu != True:
            draw_text(sc, score, 350, 50, 50)
    elif game_over:
        if score > gl_score:
            gl_score = score
            cur.execute("""update Score set score = ?;""", (str(gl_score)))
        score = 0
        sc.blit(over_display, (0, 0))
    pygame.display.update()
    sc.fill(THECOLORS['blue'])
    if not game_over and menu != True:
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

            if yc - 10 <= yb <= yc + 10:
                #cur.execute("""select name, score from Monets;""")
                #name, mone = cur.fetchone()
                mone = int(mone)
                mone += 1
                #cur.execute("""update Monets set score = ?;""", (str(mone)))
                monet = False
                print('yeeee')

            if rect_down.colliderect(rect_bird) or rect_up.colliderect(rect_bird):
                game_over = True
                print('stop')
conn.commit()
conn.close()