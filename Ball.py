from Paddle import Paddle
from settings import *
from pygame.math import Vector2
import random
import copy

class Ball(Paddle):
    """
    Ball inherits from Paddle in this project as an exercise in
    inheritance. In hindsight, both classes should inherit from a
    common GameObject base class instead.
    """
    def __init__(self, x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, width=10, height=10):
        super().__init__(x, y, width, height)
        self.velocity = Vector2(4, random.randint(2, 5))

    def update(self):
        self.position += self.velocity
        # if self.position.y < 0 or self.position.y + self.borders.y > SCREEN_HEIGHT:
        #     self.velocity.y *= -1

    def invisUpdate(self, ball):
        self.position = copy.deepcopy(ball.position)
        self.velocity = copy.deepcopy(ball.velocity)

        #Leads the ball by 100 pixels in the direction it is moving
        if self.velocity.x < 0:
            self.position.x -= 50
        else:
            self.position.x += 50
        if self.velocity.y < 0:
            self.position.y -= 50
        else:
            self.position.y += 50

        #includes bouncing off the top and bottom of the screen
        if self.position.y < 0 or self.position.y + self.borders.y > SCREEN_HEIGHT:
            self.velocity.y *= -1

        