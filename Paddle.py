import pygame
import math
import random
from settings import *
from pygame.math import Vector2




# ---------- Classes ----------
class Paddle:
    

    def __init__(self, x=   SCREEN_WIDTH-40, y=100, width=10, height=100):
        #build properties of the paddle
        self.position = Vector2(x, y)
        self.width = 0
        self.height = 0
        self.velocity = Vector2(0, 0)

        #initialize the paddle's position and size
        self.position = Vector2(x, y)
        self.borders = Vector2(width, height)
        self.velocity = Vector2(0, 0)

    def update(self ):
       
        self.position = self.position + self.velocity  
        # if self.position.y  < 0:
        #     self.velocity.y *= -1
        if self.position.y + self.borders.y > SCREEN_HEIGHT:
            self.position.y = SCREEN_HEIGHT - self.borders.y
        if self.position.y < 0:
            self.position.y = 0
        #     self.velocity.y *= -1
        # if self.position.x  < 0:
        #     self.velocity.x *= -1
        # if self.position.x + self.borders.x > SCREEN_WIDTH:
        #     self.velocity.x *= -1

    def move_up(self):
        self.position.y += -4
        self.velocity.y = -4
    def move_down(self):
        self.position.y += 4
        self.velocity.y = 4
    
    def get_rect(self):
        return pygame.Rect(self.position.x, self.position.y, self.borders.x, self.borders.y)
    
    def AI(self, ball):
        if ball.position.x - SCREEN_WIDTH /3*2 < 0 and self.position.x - SCREEN_WIDTH /3*2 < 0 or ball.position.x - SCREEN_WIDTH /3 > 0 and self.position.x - SCREEN_WIDTH /3 > 0:
            if ball.position.y < self.position.y:
                self.velocity.y = -4 * random.uniform(0.3, 1.9)
            elif ball.position.y > self.position.y + self.borders.y:
                self.velocity.y = 4 * random.uniform(0.3, 1.9)
            else:
                self.velocity.y = 0
        else:
            self.velocity.y *= 0.01
