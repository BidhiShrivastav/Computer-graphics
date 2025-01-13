import pygame
import math
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw Line Example")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)

global x1,y1,x2,y2
x1,y1,x2,y2 = 50,50,400,300
    
def rotation(x1,y1,x2,y2,t):
    t=t*(3.14/180)
    x1=x1*math.cos(t)-y1*math.sin(t)
    y1 =x1*math.sin(t)+y1*math.cos(t)
    x2=x2*math.cos(t)-y2*math.sint(t)
    y2 =x2*math.sin(t)+y2*math.cos(t)
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
    rotation(x1,y1,x2,y2,30)

    # Update the display