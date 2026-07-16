from pongMain import Paddle, Ball, Score, check_collision, collidedWithPaddle, draw_window, end, screen, handle_input
import pygame
from settings import *
import random
from pygame.math import Vector2


def main():
    rtPaddle = Paddle()
    ltPaddle = Paddle(x=30, y=100)
    tpPaddle = Paddle(y=30, x=100)
    btPaddle = Paddle(y=SCREEN_HEIGHT-30, x=100)
    ball = Ball()
    gameScore = Score()
    
    clock = pygame.time.Clock()

    
    running = True

    while running:

        # Limit FPS
        clock.tick(FPS)
        
        #move it        
        ball.update()
    
        ltPaddle.update()
        rtPaddle.update()
        tpPaddle.update()
        btPaddle.update()

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
        pygame.display.set_caption("Pong         Left Score: " + str(gameScore.leftScore) + "    Right Score: " + str(gameScore.rightScore)+ "Pong         Top Score: " + str(gameScore.topScore) + "    Bottom Score: " + str(gameScore.bottomScore))
        pygame.display.flip()

def check_game_score(ball, invisBall, gameScore, screen):
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
    if ball.position.y < 0:
        gameScore.bottomScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(random.randint(2, 6)*random.choice([-1, 1]), random.randint(2, 6)*random.choice([-1, 1]))
        invisBall.invisUpdate(ball)
    if ball.position.y > SCREEN_HEIGHT:
        gameScore.topScore += 1
        ball.position = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball.velocity = Vector2(random.randint(2, 6)*random.choice([-1, 1]), random.randint(2, 6)*random.choice([-1, 1]))
        invisBall.invisUpdate(ball)
    end(gameScore, screen)  # Check if the game is over after updating the score






if __name__ == "__main__":
    main()