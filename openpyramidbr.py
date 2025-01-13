import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1200, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Open Square Based Pyramid")

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
        #Drawing open square based pyramid
        #Square 
        draw_line_bresenham(400,400,800,400)
        draw_line_bresenham(400,400,400,800)
        draw_line_bresenham(400,800,800,800)
        draw_line_bresenham(800,800,800,400)
        #top edge
        draw_line_bresenham(400,400,600,200)
        draw_line_bresenham(600,200,800,400)
        #right edge
        draw_line_bresenham(800,400,1000,600)
        draw_line_bresenham(1000,600,800,800)
        #bottom edge
        draw_line_bresenham(800,800,600,1000)
        draw_line_bresenham(600,1000,400,800)
        #left edge
        draw_line_bresenham(400,800,200,600)
        draw_line_bresenham(200,600,400,400)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()