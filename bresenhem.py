import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1200, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a line using Bresenham's line algorithm
def draw_line_bresenham(x1, y1, x2, y2):

    if x2>x1:
        lx=1
    else:
        lx=-1
        
    if y2>y1:
        ly=1
    else:
        ly=-1

    x,y=x1,y1

    dx=abs(x2-x1)
    dy=abs(y2-y1)

    if dx>dy:
        p=2*dy-dx
        
        while(x!=x2):
           if p<0:
               x+=lx
               p+=2*dy
           else:
                x+=lx
                y+=ly
                p+=2*dy-2*dx

           screen.set_at((x,y),WHITE)
          

    else:
        p=2*dx-dy
        
        while(y!=y2):
           if p<0:
               y+=ly
           else:
                x+=lx
                y+=ly
           screen.set_at((x,y),WHITE)


# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Drawing a line using bresenham's line algorithm
        draw_line_bresenham(200,100,900,200)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()