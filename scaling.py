import pygame
import math
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Scaling")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)

global x1,y1,x2,y2
x1,y1,x2,y2 = 50,50,400,300
    
def scaling(x1,y1,x2,y2,sx,sy):
    x1 *= sx
    y1 *= sy
    x2 *= sx
    y2 *= sy
    pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 5)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw a red line (x1, y1, x2, y2, color)
    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 5)
    scaling(x1,y1,x2,y2,5,5)

    # Update the display