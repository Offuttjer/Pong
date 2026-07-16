#Jeremy Offutt 7/10/26
# This will create a simple game of pong using the turtle module in python. The game will have two paddles and a ball that bounces around the screen. The players will control the paddles using the keyboard to hit the ball back and forth. The game will keep score and display it on the screen. It will also have a single player mode where the player can play against the computer. The game will end when one player reaches a certain score.
print("start")
import pygame 
from pygame.math import Vector2
import random
import math
import copy
from Ball import Ball
from Paddle import Paddle
from Score import Score
from settings import *
from menu import show_menu
import multiplayer





# ---------- Functions ----------
def draw_window(screen, rtPaddle, ltPaddle, ball, invis, gameScore):
    """Draw everything on the screen."""
    screen.fill(BACKGROUND_COLOR)  # Clear the screen with black

    pygame.draw.rect(screen, (240, 50, 250), rtPaddle.get_rect()) # Draw the right paddle
    pygame.draw.rect(screen, (40, 50, 250), ltPaddle.get_rect()) # Draw the left paddle
    pygame.draw.rect(screen, (255, 0, 0), ball.get_rect()) # Draw the ball
    pygame.display.set_caption("Pong         Left Score: " + str(gameScore.leftScore) + "    Right Score: " + str(gameScore.rightScore))

    
    # pygame.draw.rect(screen, (50, 200, 100), invis.get_rect()) # Draw the invisble ball delete later


def handle_input(rtPaddle):
    """Handle keyboard and mouse input."""
    mousex, mousey = pygame.mouse.get_pos()

    rtPaddle.position.y = max(0, min(SCREEN_HEIGHT - rtPaddle.borders.y, rtPaddle.position.y))  # Keep paddle within screen bounds

    rtPaddle.position.y = mousey - rtPaddle.borders.y / 2  # Center the paddle on the mouse position

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
        #ensures the ball doesn't get in a straight left right loop or a straight up down loop
    if abs(ball.velocity.y) < 0.5:
        ball.velocity.y = random.randint(1, 4)
    if abs(ball.velocity.x) < 0.1:
        ball.velocity.x = random.randint(1, 4)
    end(gameScore, screen, "reg")  # Check if the game is over after updating the score

    

def end(gameScore, screen, game):
    """Check if the game is over and display the final score."""
    if gameScore.leftScore >= 5 or gameScore.rightScore >= 5 or gameScore.tpScore >= 5 or gameScore.btScore >=5:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return # Quit the game
                
                elif event.type == pygame.KEYDOWN:
            #keys = pygame.key.get_pressed()
                    if event.key ==pygame.K_ESCAPE:
                            pygame.quit()
                            return  # Quit the game
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()  # Quit the game
                    elif event.key == pygame.K_SPACE:
                        main()  # Restart the game
                    else:
                        pass
            # Fill the screen with a background color
            screen.fill(BACKGROUND_COLOR)
        
            # Create a font object
            font = pygame.font.Font(None, 74)

            title = font.render("GAME OVER", True, TEXT_COLOR)
            title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
            screen.blit(title, title_rect)

            # Render the text
            font = pygame.font.Font(None, 48)

            if game == "reg":
                lines = [
                    f"Final Score - Left: {gameScore.leftScore}   Right: {gameScore.rightScore}",
                    "",
                    "Press SPACE to play again",
                    "Press ESC to quit"
                ]
            if game == "quad":
                lines = [
                    f"Final Score - Left: {-1 *gameScore.leftScore}   Right: {-1 *gameScore.rightScore}",
                    f"Final Score - Top: {-1 *gameScore.tpScore}   Bottom: {-1 *gameScore.btScore}",
                    "",
                    "Press SPACE to play again",
                    "Press ESC to quit"
                ]

            start_y = SCREEN_HEIGHT // 2

            for i, line in enumerate(lines):
                surface = font.render(line, True, TEXT_COLOR)
                rect = surface.get_rect(center=(SCREEN_WIDTH // 2, start_y + i * 50))
                screen.blit(surface, rect)
    
            pygame.display.flip()

            
                
            

            
        

    
        


def check_collision(ball, paddle):
    """Check if the ball has collided with a paddle."""
    
    return ball.get_rect().colliderect(paddle.get_rect())

def collidedWithPaddle(ball, paddle):
    """Modifies the ball's velocity based on the paddles speed during collision."""
    if paddle.side == "left" or paddle.side == "right":
        ball.velocity.x *= -1
        if paddle.velocity.y != 0:
            ball.velocity.y +=  (paddle.velocity.y + 0.1)
    if paddle.side == "top" or paddle.side == "bottom":
        ball.velocity.y *= -1
        if paddle.velocity.x != 0:
            ball.velocity.x +=  (paddle.velocity.x + 0.1)
    ball.update()  # Update the ball's position after changing its velocity

# ---------- Main ----------
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    rtPaddle = Paddle(side="right")
    ltPaddle = Paddle(x=30, y=100, side="left")
    ball = Ball()
    invis = Ball()
    invis = copy.deepcopy(ball)
    invis.invisUpdate(ball)
    gameScore = Score()
    
    clock = pygame.time.Clock()

    choice = show_menu(screen)
    print("Menu choice:", choice)
    if(choice == "quit"):
        pygame.quit()
        exit()  # Quit the game
    if(choice == "start Multiplayer"):
        multiplayer.multiplayer(screen)
    elif (choice == "start Quadpong"):
        import quadpong
        quadpong.main(screen)
    elif (choice == "start Single Player"):
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
            check_game_score(ball, invis, gameScore, screen)
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
            
            if ball.position.y < 0 or ball.position.y > SCREEN_HEIGHT:
                ball.velocity.y *= -1

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