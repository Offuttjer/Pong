#Jeremy Offutt 7/10/26
# This will create a simple game of pong using the turtle module in python. The game will have two paddles and a ball that bounces around the screen. The players will control the paddles using the keyboard to hit the ball back and forth. The game will keep score and display it on the screen. It will also have a single player mode where the player can play against the computer. The game will end when one player reaches a certain score.
print("start")
import pygame 
from pygame.math import Vector2
import random
import math
import copy

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
        self.velocity = Vector2(0, 0)

    def update(self ):
       
        self.position = self.position + self.velocity  
        # if self.position.y  < 0:
        #     self.velocity.y *= -1
        # if self.position.y + self.borders.y > SCREEN_HEIGHT:
        #     self.velocity.y *= -1
        # if self.position.x  < 0:
        #     self.velocity.x *= -1
        # if self.position.x + self.borders.x > SCREEN_WIDTH:
        #     self.velocity.x *= -1

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

class Ball(Paddle):
    def __init__(self, x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, width=10, height=10):
        super().__init__(x, y, width, height)
        self.velocity = Vector2(4, random.randint(2, 5))

    def update(self):
        self.position += self.velocity
        if self.position.y < 0 or self.position.y + self.borders.y > SCREEN_HEIGHT:
            self.velocity.y *= -1

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

        
    
class Score:
    def __init__(self):
        self.leftScore = 0
        self.rightScore = 0




print("Welcome to Pong! Use the arrow keys to move your paddle up and down. Press 'ESCAPE' to quit the game.")


# ---------- Functions ----------
def draw_window(screen, rtPaddle, ltPaddle, ball, invis, gameScore):
    """Draw everything on the screen."""
    screen.fill((0, 0, 0))  # Clear the screen with black

    pygame.draw.rect(screen, (240, 50, 250), rtPaddle.get_rect()) # Draw the right paddle
    pygame.draw.rect(screen, (40, 50, 250), ltPaddle.get_rect()) # Draw the left paddle
    pygame.draw.rect(screen, (255, 0, 0), ball.get_rect()) # Draw the ball
    pygame.display.set_caption("Pong Left Score: " + str(gameScore.leftScore) + " Right Score: " + str(gameScore.rightScore))

    # pygame.draw.rect(screen, (50, 200, 100), invis.get_rect()) # Draw the invisble ball delete later


def handle_input(rtPaddle):
    """Handle keyboard and mouse input."""
    mousex, mousey = pygame.mouse.get_pos()

    rtPaddle.position.y = max(0, min(SCREEN_HEIGHT - rtPaddle.borders.y, rtPaddle.position.y))  # Keep paddle within screen bounds

    rtPaddle.position.y = mousey - rtPaddle.borders.y / 2  # Center the paddle on the mouse position

def check_game_score(ball, invisBall, gameScore):
    """Check if the ball has gone off the screen and update the score."""
    if ball.position.x < 0:
        gameScore.rightScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(random.randint(2, 6)*random.choice([-1, 1]), random.randint(2, 6)*random.choice([-1, 1]))
        invisBall.invisUpdate(ball)

    if ball.position.x > SCREEN_WIDTH:
        gameScore.leftScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(random.randint(2, 6)*random.choice([-1, 1]), random.randint(2, 6)*random.choice([-1, 1]))
        invisBall.invisUpdate(ball)

    #ensures the ball doesn't get in a straight left right loop or a straight up down loop
    if abs(ball.velocity.y) < 0.5:
        ball.velocity.y = random.randint(1, 4)
    if abs(ball.velocity.x) < 0.1:
        ball.velocity.x = random.randint(1, 4)
        


def check_collision(ball, paddle):
    """Check if the ball has collided with a paddle."""
    
    return ball.get_rect().colliderect(paddle.get_rect())

def collidedWithPaddle(ball, paddle):
    """Modifies the ball's velocity based on the paddles speed during collision."""
    ball.velocity.x *= -1
    if paddle.velocity.y != 0:
        ball.velocity.y +=  (paddle.velocity.y + 0.1)
    ball.update()  # Update the ball's position after changing its velocity

# ---------- Main ----------
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    rtPaddle = Paddle()
    ltPaddle = Paddle(x=30, y=100)
    ball = Ball()
    invis = Ball()
    invis = copy.deepcopy(ball)
    invis.invisUpdate(ball)
    gameScore = Score()
    
    clock = pygame.time.Clock()

    running = True

    while running:

        # Limit FPS
        clock.tick(FPS)
        
        #move it        
        ball.update()
        invis.update()
       
        rtPaddle.AI(ball)
        ltPaddle.AI(invis)
        ltPaddle.update()
        rtPaddle.update()

        #check it
        check_game_score(ball, invis, gameScore)
        if ball.velocity.x > 0 and check_collision(ball, rtPaddle): #This check-if-ball-is-moving-right fixed the issue of the ball getting stuck in the paddle when hit from the end.
            collidedWithPaddle(ball, rtPaddle)
            invis.invisUpdate(ball)
        if ball.velocity.x < 0 and check_collision(ball, ltPaddle):
            collidedWithPaddle(ball, ltPaddle)
            invis.invisUpdate(ball)
        if invis.velocity.x > 0 and check_collision(invis, rtPaddle):
            collidedWithPaddle(invis, rtPaddle)
        if invis.velocity.x < 0 and check_collision(invis, ltPaddle):
            collidedWithPaddle(invis, ltPaddle)

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Input
        handle_input(rtPaddle)

        #fix it
        # Update Game Objects
        keyboard = pygame.key.get_pressed()
        if(keyboard[pygame.K_ESCAPE]):
            running = False

        #draw it
        # Draw Everything
        draw_window(screen, rtPaddle, ltPaddle, ball, invis, gameScore)
        
        
        pygame.DOUBLEBUF
        pygame.display.flip()

    pygame.quit()


# ---------- Program Entry ----------
if __name__ == "__main__":
    main()