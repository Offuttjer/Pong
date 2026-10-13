from pongMain import check_game_score, check_collision, collidedWithPaddle, draw_window
import pygame
from settings import *
from Ball import Ball
from Paddle import Paddle
from Score import Score


def multiplayer(screen):
        rtPaddle = Paddle(side = "right")
        ltPaddle = Paddle(x=30, y=100, side = "left")
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

            #check it
            check_game_score(ball, ball, gameScore, screen)
            if ball.velocity.x > 0 and check_collision(ball, rtPaddle): #This check-if-ball-is-moving-right fixed the issue of the ball getting stuck in the paddle when hit from the end.
                collidedWithPaddle(ball, rtPaddle)
            if ball.velocity.x < 0 and check_collision(ball, ltPaddle):
                collidedWithPaddle(ball, ltPaddle)
            if ball.position.y < 0 or ball.position.y > SCREEN_HEIGHT:
                ball.velocity.y *= -1

            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Input
            handle_input(ltPaddle, rtPaddle)

            #fix it
            # Update Game Objects
            keyboard = pygame.key.get_pressed()
            if(keyboard[pygame.K_ESCAPE]):
                running = False

            #draw it
            screen.fill(BACKGROUND_COLOR)
            draw_window(screen, ltPaddle, rtPaddle, ball, ball, gameScore)
            pygame.display.set_caption("Pong         Left Score: " + str(gameScore.leftScore) + "    Right Score: " + str(gameScore.rightScore))
            pygame.display.flip()

def handle_input(ltPaddle, rtPaddle):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ltPaddle.move_up()
    if keys[pygame.K_s]:
        ltPaddle.move_down()
    if keys[pygame.K_UP]:
        rtPaddle.move_up()
    if keys[pygame.K_DOWN]:
        rtPaddle.move_down()