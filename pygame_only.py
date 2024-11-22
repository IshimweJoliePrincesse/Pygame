import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Movement Example")

# Set up the player
player_color = (255, 0, 0)  # Red color
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height // 2 - player_height // 2
player_speed = 5

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Prevent the player from going out of bounds
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - player_height:
        player_y = screen_height - player_height

    # Fill the screen with a color (white)
    screen.fill((255, 255, 255))

    # Draw the player (red square)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
