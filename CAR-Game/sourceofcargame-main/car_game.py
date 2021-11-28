import random
from time import sleep

import pygame


class CarRacing:
    def __init__(self):
        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None
        self.intialize()

    def intialize(self):
        self.crashed = False
        self.carImg = pygame.image.load("img/red_car.png")
        self.car_x_co = (self.display_width * 0.45)
        self.car_y_co = (self.display_height * 0.8)
        self.car_width = 49

        self.enemy = pygame.image.load("img/selver_car.png")
        self.enemy_x_co = random.randrange(230, 510)
        self.enemy_y_co = 0-random.randrange(10, 600)
        self.enemy_speed = 5
        self.enemy_width = 49
        self.enemy_hieght = 100

        self.bgImg = pygame.image.load("img/asphelt.jpg")
        self.bg_x1 = (self.display_width / 2) - (400 / 2)
        self.bg_x2 = (self.display_width / 2) - (400 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 9
        self.count = 0

    def car(self, car_x_co, car_y_co):
        self.gameDisplay.blit(self.carImg, (car_x_co, car_y_co))

    def racing_window(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("car racing game")
        self.run_car()

    def run_car(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

                if (event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        self.car_x_co -= 50
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        self.car_x_co += 50

            self.gameDisplay.fill(self.black)
            self.back_ground_road()
            self.run_enemy_car(self.enemy, self.enemy_x_co, self.enemy_y_co)
            self.enemy_y_co += self.enemy_speed

            if self.enemy_y_co > self.display_height:
                self.enemy_y_co = 0 - self.enemy_hieght
                self.enemy_x_co = random.randrange(230, 510)

            self.car(self.car_x_co, self.car_y_co)
            self.highscore(self.count)
            self.count += 0.5
            if self.count % 100 == 0:
                self.enemy_speed += 1

                self.bg_speed += 1

            if self.car_y_co < self.enemy_y_co + self.enemy_hieght - 2:
                if self.car_x_co > self.enemy_x_co - self.enemy_width + 5 and self.car_x_co < self.enemy_x_co + self.enemy_width - 5:
                    self.crashed = True

            if self.car_x_co < 230 or self.car_x_co > 510:
                self.crashed = True

            pygame.display.update()
            self.clock.tick(60)

    def back_ground_road(self):
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))
        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_enemy_car(self, enemy, thingx, thingy):
        self.gameDisplay.blit(enemy, (thingx, thingy))

    def highscore(self, count):
        font = pygame.font.SysFont("Times New Roman", 20)
        text = font.render('score :' + str(count), True, self.white)
        self.gameDisplay.blit(text, (0, 0))

    def display_credit(self):
        font = pygame.font.SysFont("Times New Roman", 14)
        text = font.render('thanks for playing', True, self.white)
        self.gameDisplay.blit(text, (600, 500))
        text = font.render("Yousef Alramli", True, self.white)
        self.gameDisplay.blit(text, (600, 500))


if __name__ == "__main__":
    car_racing = CarRacing()
    car_racing.racing_window()