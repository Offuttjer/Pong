import pygame
import settings

def show_menu(screen):

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               exit() 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "start Single Player"
                if event.key == pygame.K_m:
                    return "start Multiplayer"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()  # Quit the game

        # Fill the screen with a background color
        screen.fill(settings.BACKGROUND_COLOR)
       
        # Create a font object
        font = pygame.font.Font(None, 74)

        title = font.render("PONG", True, settings.TEXT_COLOR)
        title_rect = title.get_rect(center=(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 4))
        screen.blit(title, title_rect)

        # Render the text
        text = title
        text_rect = text.get_rect(center=(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 4))
        screen.blit(text, text_rect)

        # Render the instructions
        instruction_font = pygame.font.Font(None, 36)
        instructions = [
            "First to 5 wins",
            "Press SPACE to Start Single Player",
            "Press M to Start Multiplayer, Game to 10",
            "Press ESC to Quit"
            
        ]

        for i, instruction in enumerate(instructions):
            instruction_text = instruction_font.render(instruction, True, settings.TEXT_COLOR)
            instruction_rect = instruction_text.get_rect(center=(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 + i * 40))
            screen.blit(instruction_text, instruction_rect)
        # Draw Everything
        # screen.fill(settings.BACKGROUND_COLOR)
        pygame.display.set_caption("Pong         Left Score: " + str(0) + "    Right Score: " + str(0))
        
        
        pygame.DOUBLEBUF
        pygame.display.flip()

    pygame.quit()

   