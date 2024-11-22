import pygame
import serial
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Control LED with Pygame")

# Initialize serial communication with Arduino (adjust port as necessary)
ser = serial.Serial('COM3', 9600)  # COM3 for Windows or '/dev/ttyACM0' for Linux

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ser.write(b'1')  # Send '1' to turn the LED on
    elif keys[pygame.K_DOWN]:
        ser.write(b'0')  # Send '0' to turn the LED off

    # Fill the screen with a color (white)
    screen.fill((255, 255, 255))

    # Display instructions on the screen
    font = pygame.font.Font(None, 36)
    text = font.render("Use UP/DOWN arrows to control LED", True, (0, 0, 0))
    screen.blit(text, (50, screen_height // 2))

    # Update the display
    pygame.display.update()

# Close the serial connection and quit Pygame
ser.close()
pygame.quit()
sys.exit()
