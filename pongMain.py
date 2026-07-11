#Jeremy Offutt 7/10/26
# This will create a simple game of pong using the turtle module in python. The game will have two paddles and a ball that bounces around the screen. The players will control the paddles using the keyboard to hit the ball back and forth. The game will keep score and display it on the screen. It will also have a single player mode where the player can play against the computer. The game will end when one player reaches a certain score.

import pygame 
from pygame.math import Vector2
import random
import math

# ---------- Constants ----------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

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

    def update(self ):
       
        self.position = self.position + self.velocity  
        if self.position.y  < 0:
            self.velocity.y *= -1
        if self.position.y + self.borders.y > SCREEN_HEIGHT:
            self.velocity.y *= -1
    #    if self.position.x  < 0:
     #       self.velocity.x *= -1
      #  if self.position.x + self.borders.x > SCREEN_WIDTH:
       #     self.velocity.x *= -1

    def get_paddle(self):
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

class Ball(Paddle):
    def __init__(self, x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, width=10, height=10):
        super().__init__(x, y, width, height)
        self.velocity = Vector2(4, 4)

    def update(self):
        self.position += self.velocity
        if self.position.y < 0 or self.position.y + self.borders.y > SCREEN_HEIGHT:
            self.velocity.y *= -1
        
    
class Score:
    def __init__(self):
        self.leftScore = 0
        self.rightScore = 0




print("Welcome to Pong! Use the arrow keys to move your paddle up and down. Press 'ESCAPE' to quit the game.")


# ---------- Functions ----------
def draw_window(screen, rtPaddle, ltPaddle, ball, gameScore):
    """Draw everything on the screen."""
    screen.fill((0, 0, 0))  # Clear the screen with black

    pygame.draw.rect(screen, (240, 50, 250), rtPaddle.get_paddle()) # Draw the right paddle
    pygame.draw.rect(screen, (40, 50, 250), ltPaddle.get_paddle()) # Draw the left paddle
    pygame.draw.rect(screen, (255, 0, 0), ball.get_paddle()) # Draw the ball
    pygame.display.set_caption("Pong Left Score: " + str(gameScore.leftScore) + " Right Score: " + str(gameScore.rightScore))


def handle_input():
    """Handle keyboard and mouse input."""
    pass

def check_game_score(ball, gameScore):
    """Check if the ball has gone off the screen and update the score."""
    if ball.position.x < 0:
        gameScore.rightScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(4, 4)
    if ball.position.x > SCREEN_WIDTH:
        gameScore.leftScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(-4, 4)

def check_collision(ball, paddle):
    """Check if the ball has collided with a paddle."""
    
    return ball.get_paddle().colliderect(paddle.get_paddle())

# ---------- Main ----------
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    rtPaddle = Paddle()
    ltPaddle = Paddle(x=30, y=100)
    ball = Ball()
    gameScore = Score()
    
    clock = pygame.time.Clock()

    running = True

    while running:

        # Limit FPS
        clock.tick(FPS)
        
        #move it
       # rtPaddle.update(Vector2(1, 1))
       
        
        ball.update()
        rtPaddle.AI(ball)
        ltPaddle.AI(ball)
        ltPaddle.update()
        rtPaddle.update()

        #check it
        check_game_score(ball, gameScore)
        if check_collision(ball, rtPaddle) or check_collision(ball, ltPaddle):
            ball.velocity.x *= -1

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Input
        handle_input()

        #fix it
        # Update Game Objects
        keyboard = pygame.key.get_pressed()
        if(keyboard[pygame.K_ESCAPE]):
            running = False

        #draw it
        # Draw Everything
        draw_window(screen, rtPaddle, ltPaddle, ball, gameScore)
        
        pygame.display.flip()

    pygame.quit()


# ---------- Program Entry ----------
if __name__ == "__main__":
    main()