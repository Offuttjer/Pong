from pongMain import Paddle, Ball, Score, check_collision, collidedWithPaddle, draw_window, end
import pygame
from settings import *
import random
from pygame.math import Vector2


def main(screen):
    rtPaddle = Paddle(side ="right")
    ltPaddle = Paddle(x=30, y=100, side = "left")
    tpPaddle = Paddle(y=30, x=100, width=100, side="top", height=10)
    btPaddle = Paddle(y=SCREEN_HEIGHT-30, x=100, width=100, side="bottom", height=10)
    ball = Ball()
    gameScore = Score()
    
    clock = pygame.time.Clock()

    
    running = True

    while running:

        # Limit FPS
        clock.tick(FPS)
        
        #move it        
        ball.update()
    
        old_pos = ltPaddle.position.copy()
        ltPaddle.update()
        if ltPaddle.get_rect().colliderect(tpPaddle.get_rect()) or ltPaddle.get_rect().colliderect(btPaddle.get_rect()):
            ltPaddle.position = old_pos
       
        old_pos = rtPaddle.position.copy()
        rtPaddle.update()
        if rtPaddle.get_rect().colliderect(tpPaddle.get_rect()) or rtPaddle.get_rect().colliderect(btPaddle.get_rect()):
            rtPaddle.position = old_pos
        
        old_pos = tpPaddle.position.copy()
        tpPaddle.update()
        if tpPaddle.get_rect().colliderect(ltPaddle.get_rect()) or tpPaddle.get_rect().colliderect(rtPaddle.get_rect()):
            tpPaddle.position = old_pos
       
        old_pos = btPaddle.position.copy()
        btPaddle.update()
        if btPaddle.get_rect().colliderect(ltPaddle.get_rect()) or btPaddle.get_rect().colliderect(rtPaddle.get_rect()):
            btPaddle.position = old_pos
        

        #check it
        check_game_score(ball, ball, gameScore, screen)
        if ball.velocity.x > 0 and check_collision(ball, rtPaddle): #This check-if-ball-is-moving-right fixed the issue of the ball getting stuck in the paddle when hit from the end.
            collidedWithPaddle(ball, rtPaddle)
        if ball.velocity.x < 0 and check_collision(ball, ltPaddle):
            collidedWithPaddle(ball, ltPaddle)
        if ball.velocity.y > 0 and check_collision(ball, btPaddle):
            collidedWithPaddle(ball, btPaddle)
        if ball.velocity.y < 0 and check_collision(ball, tpPaddle):
            collidedWithPaddle(ball, tpPaddle)

        # if ltPaddle.get_rect().colliderect(tpPaddle.get_rect()):
        #     ltPaddle.position.y = 35#tpPaddle.position.y - tpPaddle.borders.y
        # if ltPaddle.get_rect().colliderect(btPaddle.get_rect()) :
        #     ltPaddle.position.y = btPaddle.position.y + ltPaddle.borders.y
        # if rtPaddle.get_rect().colliderect(tpPaddle.get_rect()):     
        #     rtPaddle.position.y = 35#tpPaddle.position.y - tpPaddle.borders.y   
        # if rtPaddle.get_rect().colliderect(btPaddle.get_rect()) :
        #     rtPaddle.position.y = btPaddle.position.y + rtPaddle.borders.y

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Input
        handle_input(ltPaddle, rtPaddle, tpPaddle, btPaddle)

        #fix it
        # Update Game Objects
        keyboard = pygame.key.get_pressed()
        if(keyboard[pygame.K_ESCAPE]):
            running = False

        #draw it
        screen.fill(BACKGROUND_COLOR)
        draw_window(screen, ltPaddle, rtPaddle, tpPaddle, btPaddle, ball, ball, gameScore)
        pygame.display.set_caption("Pong         Left Score: " + str(-1*gameScore.leftScore) + "    Right Score: " + str(-1*gameScore.rightScore)+ "        Top Score: " + str(-1*gameScore.tpScore) + "    Bottom Score: " + str(-1*gameScore.btScore))
        pygame.display.flip()

def check_game_score(ball, invisBall, gameScore, screen):
    """Check if the ball has gone off the screen and update the score."""
    if ball.position.x < 0:
        gameScore.leftScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(random.randint(2, 6)*random.choice([-1, 1]), random.randint(2, 6)*random.choice([-1, 1]))
        invisBall.invisUpdate(ball)

    if ball.position.x > SCREEN_WIDTH:
        gameScore.rightScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(random.randint(2, 6)*random.choice([-1, 1]), random.randint(2, 6)*random.choice([-1, 1]))
        invisBall.invisUpdate(ball)

    if ball.position.y < 0:
        gameScore.tpScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(random.randint(2, 6)*random.choice([-1, 1]), random.randint(2, 6)*random.choice([-1, 1]))
        invisBall.invisUpdate(ball)

    if ball.position.y > SCREEN_HEIGHT:
        gameScore.btScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(random.randint(2, 6)*random.choice([-1, 1]), random.randint(2, 6)*random.choice([-1, 1]))
        invisBall.invisUpdate(ball)

    if abs(ball.velocity.x) < 0.5 or abs(ball.velocity.x) < 0.5:
        ball.velocity = random.randint(1, 4)
    end(gameScore, screen, "quad")  # Check if the game is over after updating the score


# ---------- Functions ----------
def draw_window(screen, rtPaddle, ltPaddle, tpPaddle, btPaddle, ball, invis, gameScore):
    """Draw everything on the screen."""
    screen.fill(BACKGROUND_COLOR)  # Clear the screen with black

    pygame.draw.rect(screen, (240, 50, 250), rtPaddle.get_rect()) # Draw the right paddle
    pygame.draw.rect(screen, (40, 50, 250), ltPaddle.get_rect()) # Draw the left paddle
    pygame.draw.rect(screen, (20, 150, 250), tpPaddle.get_rect()) # Draw the top paddle
    pygame.draw.rect(screen, (240, 250, 0), btPaddle.get_rect()) # Draw the bottom paddle
    pygame.draw.circle(
            screen,
            (255,0,0),
            (
                int(ball.position.x + ball.borders.x/2),
                int(ball.position.y + ball.borders.y/2)
            ),
            int(ball.borders.x/2)
        )# Draw the ball

    pygame.draw.rect(screen, (50, 200, 100), invis.get_rect()) # Draw the invisble ball delete later

def handle_input(left, right, top, bottom):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left.move_up()
    if keys[pygame.K_s]:
        left.move_down()
    if keys[pygame.K_UP]:
        right.move_up()
    if keys[pygame.K_DOWN]:
        right.move_down()
    if keys[pygame.K_v]:
        bottom.move_left()
    if keys[pygame.K_b]:
        bottom.move_right()
    if keys[pygame.K_5]:
        top.move_left()
    if keys[pygame.K_6]:
        top.move_right();
    


if __name__ == "__main__":
    main()