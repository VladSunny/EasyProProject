import pygame
from pygame.colordict import THECOLORS
from random import randint
import random
import sys
import time





game_over = False
#musik_bird = pygame.mixer.Sound('bird.WAV')
ypbchk = pygame.image.load('lol_b.png')
plane = pygame.image.load('plane.png')
plane = pygame.transform.scale(plane, (250, 250))
ypbchk = pygame.transform.scale(ypbchk, (150, 150))
b = 0
bch = False
xb, yb = 650, 10
m = 0
mt = True
zbz = 1
mad = 0
madt = True
hat_meny = False
gamers = 1
#допустим opat

hat1rl = pygame.image.load('hat1_for_lolb.png')
hat1ud = pygame.transform.rotate(hat1rl, 90)
hat2rl = pygame.image.load('hat2_for_lolb.png')
hat2ud = pygame.transform.rotate(hat2rl, 90)
hat3rl = pygame.image.load('hat3_for_lolb.png')
hat3ud = pygame.transform.rotate(hat3rl, 90)
bootsu = pygame.image.load('boots_for_pp.png')
bootsu.set_colorkey(THECOLORS['gray'])
#bootsu.set_color('gray')
bootsd = pygame.transform.rotate(bootsu, 180)
bootsl = pygame.transform.rotate(bootsu, 270)
bootsr = pygame.transform.rotate(bootsu, 90)
chipd = pygame.image.load('chip_for_pg.png')
chipu = pygame.transform.rotate(chipd, 180)
chipr = pygame.transform.rotate(chipd, 90)
chipl = pygame.transform.rotate(chipd, 270)
plashu = pygame.image.load('plash_for_gp.png')
plashd = pygame.transform.rotate(plashu, 180)
plashr = pygame.transform.rotate(plashu, 270)
plashl = pygame.transform.rotate(plashu, 90)


now_hat = 0
now_pop = 0
t = False
fdf = 0

class Game:
    def set_surface_and_title(self):
        """Задаем surface(поверхность поверх которой будет все рисоваться)
        и устанавливаем загаловок окна"""
        self.play_surface = pygame.display.set_mode((
            self.screan_widght, self.screan_height))
        pygame.display.set_caption('Snake Game')

    def __init__(self):
        self.screan_widght = 700
        self.screan_height = 700
        self.screan_color = 'green'
        self.FPS_contoll = pygame.time.Clock()
        self.score = 0

    def event_look(self, change_too):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                game_over = True
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w:
                    change_too = 'UP'
                elif i.key == pygame.K_a:
                    change_too = 'LEFT'
                elif i.key == pygame.K_d:
                    change_too = 'RIGHT'
                elif i.key == pygame.K_s:
                    change_too = 'DOWN'


        return change_too

    def refresh_display(self):
        pygame.display.update()
        self.sc.fill(THECOLORS['purple'])
        pygame.time.delay(FPS)

    def create_surface(self):
        pygame.init()
        self.sc = pygame.display.set_mode((self.screan_widght, self.screan_height))
        self.sc.fill(THECOLORS['green'])

    def _game_over_(self):
        font = pygame.font.SysFont('arial', (50))
        text_size = font.render(f'Your scor are: {self.score}', True,THECOLORS['black'], )
        rect = text_size.get_rect()
        rect.midtop = (50, 50)
        self.sc.blit(text_size, rect)
        pygame.quit()
        sys.exit()

    def init_and_check_for_errors(self):
        """Начальная функция для инициализации и
           проверки как запустится pygame"""
        check_errors = pygame.init()
        if check_errors[1] > 0:
            uyywsy = 0
            sys.exit()
        else:
            print('Ok')
    def draw_text(self, text, sc, x, y, size):
        font = pygame.font.SysFont('arial', size)
        text1 = font.render(text, 1, THECOLORS['green'])
        sc.blit(text1, (x, y))
    def musik_play(self, pyt):
        musik = pygame.mixer.Sound(pyt)
        musik.play()
    def musik_stop(self, pyt):
        musik = pygame.mixer.Sound(pyt)
        musik.stop()



class Gusenica():
    def __init__(self, color):
        self.head_gusenica_poz = [100, 50]
        self.gusenica_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50]]
        self.gusenica_color = color
        self.direction = 'DOWN'
        self.change_too = 'DOWN'
        self.gusenica_spid = 5


    def validate_direction_and_change(self):
        """Изменияем направление движения змеи только в том случае,
        если оно не прямо противоположно текущему"""
        if any((self.change_too == "RIGHT" and not self.direction == "LEFT",
                self.change_too == "LEFT" and not self.direction == "RIGHT",
                self.change_too == "UP" and not self.direction == "DOWN",
                self.change_too == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_too

    def change_head_pozition(self):
        if self.direction == 'RIGHT':
            self.head_gusenica_poz[0] += self.gusenica_spid
        if self.direction == 'LEFT':
            self.head_gusenica_poz[0] -= self.gusenica_spid
        if self.direction == 'UP':
            self.head_gusenica_poz[1] -= self.gusenica_spid
        if self.direction == 'DOWN':
            self.head_gusenica_poz[1] += self.gusenica_spid

    def gusenica_body_mexanizm(self, score, apple_poz, screan_widght, screan_height):

        self.gusenica_body.insert(0, list(self.head_gusenica_poz))
        if not (apple_poz[0] - 6 <= self.head_gusenica_poz[0] <= apple_poz[0] + 6 and apple_poz[1] - 6 <= self.head_gusenica_poz[1] <= apple_poz[1] + 6):
            self.gusenica_body.pop()
        else:
            score += 1
            apple_poz = [randint(100,600), randint(100, 600)]
        return apple_poz, score


    def draw_snake(self, sc, color, hat1rl, hat2rl, hat3rl, hat1ud, hat2ud, hat3ud,):
        global bootsu
        global bootsd
        global bootsl
        global bootsr
        global plashd
        global plashl
        global plashr
        global plashu
        global chipl
        global chipr
        global chipu
        global chipd
        global gamers
        sc.fill(THECOLORS[color])
        for poz in self.gusenica_body:
            pygame.draw.circle(sc, THECOLORS[self.gusenica_color], (poz[0], poz[1]), 7)
        if gamers == 2:
            for poz in gusinuchka_2.gusenica_body:
                pygame.draw.circle(sc, THECOLORS[gusinuchka_2.gusenica_color], (poz[0], poz[1]), 7)
        poz = self.gusenica_body[0]
        pygame.draw.circle(sc, THECOLORS['grey'], (poz[0], poz[1]), 6)
        pygame.draw.circle(sc, THECOLORS['black'], (poz[0], poz[1]), 3)
        if gamers == 2:
            poz = gusinuchka_2.gusenica_body[0]
            pygame.draw.circle(sc, THECOLORS['grey'], (poz[0], poz[1]), 6)
            pygame.draw.circle(sc, THECOLORS['black'], (poz[0], poz[1]), 3)
        hat1rl = pygame.transform.scale(hat1rl, (20, 20))
        hat2rl = pygame.transform.scale(hat2rl, (20, 20))
        hat3rl = pygame.transform.scale(hat3rl, (20, 20))
        hat1ud = pygame.transform.scale(hat1ud, (20, 20))
        hat2ud = pygame.transform.scale(hat2ud, (20, 20))
        hat3ud = pygame.transform.scale(hat3ud, (20, 20))
        bootsu = pygame.transform.scale(bootsu, (20, 20))
        bootsd = pygame.transform.scale(bootsd, (20, 20))
        bootsl = pygame.transform.scale(bootsl, (20, 20))
        bootsr = pygame.transform.scale(bootsr, (20, 20))
        chipd = pygame.transform.scale(chipd, (20, 20))
        chipu = pygame.transform.scale(chipu, (20, 20))
        chipr = pygame.transform.scale(chipr, (20, 20))
        chipl = pygame.transform.scale(chipl, (20, 20))
        plashu = pygame.transform.scale(plashu, (20, 20))
        plashd = pygame.transform.scale(plashd, (20, 20))
        plashr = pygame.transform.scale(plashr, (20, 20))
        plashl = pygame.transform.scale(plashl, (20, 20))
        if snake.direction == 'RIGHT' or snake.direction == 'LEFT':
            if now_hat == 1:
                game.play_surface.blit(hat2rl, (poz[0] - 10, poz[1] - 20))
            elif now_hat == 2:
                game.play_surface.blit(hat1rl, (poz[0] - 10, poz[1] - 20))
            elif now_hat == 3:
                game.play_surface.blit(hat3rl, (poz[0] - 10, poz[1] - 20))
        if snake.direction == 'UP' or snake.direction == 'DOWN':
            if now_hat == 1:
                game.play_surface.blit(hat2ud, (poz[0] - 20, poz[1] - 10))
            elif now_hat == 2:
                game.play_surface.blit(hat1ud, (poz[0] - 20, poz[1] - 10))
            elif now_hat == 3:
                game.play_surface.blit(hat3ud, (poz[0] - 20, poz[1] - 10))
        poz = self.gusenica_body[len(self.gusenica_body) - 1]
        if snake.direction == 'RIGHT':
            if now_pop == 1:
                game.play_surface.blit(plashr, (poz[0] - 10, poz[1] - 15))
            if now_pop == 2:
                game.play_surface.blit(bootsr, (poz[0] - 10, poz[1] - 15))
            if now_pop == 3:
                game.play_surface.blit(chipr, (poz[0] - 10, poz[1] - 15))
        if snake.direction == 'LEFT':
            if now_pop == 1:
                game.play_surface.blit(plashl, (poz[0] - 10, poz[1] - 15))
            if now_pop == 2:
                game.play_surface.blit(bootsl, (poz[0] - 10, poz[1] - 15))
            if now_pop == 3:
                game.play_surface.blit(chipl, (poz[0] - 10, poz[1] - 15))
        if snake.direction == 'UP':
            if now_pop == 1:
                game.play_surface.blit(plashu, (poz[0] - 15, poz[1] - 15))
            if now_pop == 2:
                game.play_surface.blit(bootsu, (poz[0] - 15, poz[1] - 15))
            if now_pop == 3:
                game.play_surface.blit(chipu, (poz[0] - 15, poz[1] - 15))
        if snake.direction == 'DOWN':
            if now_pop == 1:
                game.play_surface.blit(plashd, (poz[0] - 15, poz[1] - 15))
            if now_pop == 2:
                game.play_surface.blit(bootsd, (poz[0] - 15, poz[1] - 15))
            if now_pop == 3:
                game.play_surface.blit(chipd, (poz[0] - 15, poz[1] - 15))




    def check_wals_floors(self, screan_widght, screen_height, game_over):
        if not screan_widght - screan_widght <= self.head_gusenica_poz[0] <= screan_widght and screen_height - screen_height <= self.head_gusenica_poz[1] <= screen_height:
             game_over()

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        """Проверка, что столкунлись с концами экрана или сами с собой
        (змея закольцевалась)"""
        global gamers
        if any((
            self.head_gusenica_poz[0] > screen_width-10
            or self.head_gusenica_poz[0] < 0,
            self.head_gusenica_poz[1] > screen_height-10
            or self.head_gusenica_poz[1] < 0
                )):
            game_over()
        if gamers == 2:
            if any((
                gusinuchka_2.head_gusenica_poz[0] > screen_width-10
                or gusinuchka_2.head_gusenica_poz[0] < 0,
                gusinuchka_2.head_gusenica_poz[1] > screen_height-10
                or gusinuchka_2.head_gusenica_poz[1] < 0
                    )):
                gamers = 1
        for block in self.gusenica_body[1:]:
            # проверка на то, что первый элемент(голова) врезался в
            # любой другой элемент змеи (закольцевались)
              if (block[0] == self.head_gusenica_poz[0] and
                    block[1] == self.head_gusenica_poz[1]):
                game_over()
                # сложно

class Food():
    def __init__(self, food_color, screen_width, screen_height):
        """Инит еды"""
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_poz = [random.randrange(1, screen_width/10)*10,
                         random.randrange(1, screen_height/10)*10]
        print(self.food_poz)

    def draw_food(self, play_surface):
        """Отображение еды"""
        pygame.draw.rect(
            play_surface, self.food_color, pygame.Rect(
                (self.food_poz),  #Ошибся в названии поля не food_poz, а food_pos какая-то тут странная ошибка нужно поразмышлять
                (self.food_size_x, self.food_size_y)))



RDS = 13
FPS = 60

game = Game()
snake = Gusenica('green') #при создании экземпляра класса необходимо передать цвет
gusinuchka_2 = Gusenica('red')
food = Food(THECOLORS['red'], game.screan_widght, game.screan_height)

game.init_and_check_for_errors()
game.set_surface_and_title()
game.create_surface()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game._game_over_()
        if i.type == pygame.QUIT:
            game_over = True
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                snake.change_too = 'UP'
            elif i.key == pygame.K_a:
                snake.change_too = 'LEFT'
            elif i.key == pygame.K_d:
                snake.change_too = 'RIGHT'
            elif i.key == pygame.K_s:
                snake.change_too = 'DOWN'
            if i.key == pygame.K_SPACE:
                if not hat_meny:
                    hat_meny = True
                else:
                    hat_meny = False
            if i.key == pygame.K_1 and hat_meny and game.score >= 10:
                game.score -= 10
                now_hat = 1
            elif game.score <= 10 and hat_meny:
                t = True
            if i.key == pygame.K_2 and hat_meny and game.score >= 20:
                game.score -= 20
                now_hat = 2
            elif game.score <= 20 and hat_meny:
                t = True
            if i.key == pygame.K_3 and hat_meny and game.score >= 40:
                game.score -= 40
                now_hat = 3
            elif game.score <= 40 and hat_meny:
                t = True
            if i.key == pygame.K_4 and hat_meny and game.score >= 10:
                game.score -= 10
                now_pop = 1
            elif game.score <= 10 and hat_meny:
                t = True
            if i.key == pygame.K_5 and hat_meny and game.score >= 20:
                game.score -= 20
                now_pop = 2
            elif game.score <= 20 and hat_meny:
                t = True
            if i.key == pygame.K_6 and hat_meny and game.score >= 40:
                game.score -= 40
                now_pop = 3
            elif game.score <= 40 and hat_meny:
                t = True
            if i.key == pygame.K_F2 and gamers == 1:
                gamers = 2
                print(gamers)
            elif i.key == pygame.K_F2 and gamers == 2:
                gamers = 1
            if gamers == 2:
                if i.key == pygame.K_UP:
                    gusinuchka_2.change_too = 'UP'
                elif i.key == pygame.K_LEFT:
                    gusinuchka_2.change_too = 'LEFT'
                elif i.key == pygame.K_RIGHT:
                    gusinuchka_2.change_too = 'RIGHT'
                elif i.key == pygame.K_DOWN:
                    gusinuchka_2.change_too = 'DOWN'

            print(snake.change_too)
            print(snake.direction)
    if not bch:
        snake.change_to = game.event_look(snake.change_too)
        if gamers == 2:
            gusinuchka_2.change_to = game.event_look(gusinuchka_2.change_too)
        if not hat_meny:
            snake.validate_direction_and_change()
            snake.change_head_pozition()
            if gamers == 2:
                gusinuchka_2.validate_direction_and_change()
                gusinuchka_2.change_head_pozition()
                food.food_poz, game.score = gusinuchka_2.gusenica_body_mexanizm(game.score, food.food_poz, game.screan_widght,
                                                                         game.screan_height)
            food.food_poz, game.score = snake.gusenica_body_mexanizm(game.score, food.food_poz, game.screan_widght, game.screan_height)
    							#здесь у тебя было Gusenica.gusenica_body_mexanizm


    							#А нужно вызывать функцию от созданного объекта



    if game.score >= 50:
         bch = True

    if m == 1 and mt:
        game.musik_play('bird.WAV')
        mt = False

    if not bch and not hat_meny:
        snake.draw_snake(game.play_surface, 'purple', hat1rl, hat2rl, hat3rl, hat1ud, hat2ud, hat3ud)# передаешь вместо цвета объект game
        food.draw_food(game.play_surface)

    snake.check_for_boundaries(
        game._game_over_, game.screan_widght, game.screan_height)
    time.sleep(0)
    if zbz <= 100 and bch:
        game.play_surface.blit(plane, (xb, yb))
        xb -= 6
        game.play_surface.blit(ypbchk, (10, 10))
        zbz += 1

        if zbz >= 101:
            zbz = 101

    if mad == 1 and madt:
        madt = False
        game.musik_play('porovozik_is_ada.WAV')

    if bch and zbz != 21:
        m = 1

    if bch and zbz == 101:
        game.musik_stop('bird.WAV')
        mad = 1
        game.play_surface.blit(ypbchk, (10, 10))
        ypbchk = pygame.transform.rotate(ypbchk, -1)

    if hat_meny:
        hat1rl = pygame.transform.scale(hat1rl, (200, 100))
        hat2rl = pygame.transform.scale(hat2rl, (200, 100))
        hat3rl = pygame.transform.scale(hat3rl, (200, 100))
        bootsu = pygame.transform.scale(bootsu, (200, 200))
        chipd = pygame.transform.scale(chipd, (200, 200))
        plashu = pygame.transform.scale(plashu, (200, 200))
        game.play_surface.blit(hat2rl, (100, 250))
        game.play_surface.blit(hat1rl, (300, 250))
        game.play_surface.blit(hat3rl, (500, 250))
        game.play_surface.blit(bootsu, (300, 500))
        game.play_surface.blit(chipd, (500, 500))
        game.play_surface.blit(plashu, (100, 500))
        game.draw_text('10', game.play_surface, 200, 200, 40)
        game.draw_text('20', game.play_surface, 400, 200, 40)
        game.draw_text('40', game.play_surface, 600, 200, 40)
        game.draw_text('10', game.play_surface, 200, 450, 40)
        game.draw_text('20', game.play_surface, 400, 450, 40)
        game.draw_text('40', game.play_surface, 600, 450, 40)

    if t and fdf != 10:
        print(1)
        fdf += 1
        game.draw_text('you dont have enough coins', game.play_surface, 350, 500, 30)
    else:
        t = False
        fdf = 0


    game.draw_text(f'game score = {game.score}', game.play_surface, 30, 30, 30)
    game.refresh_display()
