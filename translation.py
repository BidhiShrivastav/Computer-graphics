# Translation
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Translation of a line")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a circle using the 2D Algorithm
def draw(x1,y1, x2, y2):
    dx=x2-x1
    dy=y2-y1 
    if abs(dx)>abs(dy):
        step=abs(dx)
    else:
        step=abs(dy)
    xinc=dx/step
    yinc=dy/step
    x=x1
    y=y1
    screen.set_at((round(x),round(y)),WHITE)
    for i in range(step):
        x=x+xinc
        y=y+yinc
        screen.set_at((round(x),round(y)),WHITE)
def main():
    x1,y1=100,100
    x2,y2=400,300
    tx=50
    ty=50
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)
        draw(x1,y1,x2,y2)
        draw(x1+tx,y1+ty,x2+tx,y2+ty)
    

        pygame.display.flip()

if __name__ == "__main__":
    main()