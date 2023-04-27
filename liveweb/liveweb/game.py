pip install pygame
import pygame
import time

pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption for the game
pygame.display.set_caption("Snake Game")

# Define the snake block size
block_size = 10

# Define the clock object
clock = pygame.time.Clock()

# Define the font object
font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
    """
    Displays a message on the screen
    """
    msg_text = font_style.render(msg, True, color)
    screen.blit(msg_text, [screen_width / 6, screen_height / 3])


def game_loop():
    """
    Main game loop
    """
    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Fill the screen with white color
        screen.fill(white)

        # Display the message "Welcome to Snake Game"
        message("Welcome to Snake Game", black)

        # Update the screen
        pygame.display.update()

        # Set the frames per second
        clock.tick(10)

    # Quit the game
    pygame.quit()
    quit()


# Call the game loop function
game_loop()

