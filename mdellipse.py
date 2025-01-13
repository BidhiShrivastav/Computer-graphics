import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Mid-point Ellipse Algorithm")

# Colors
CIRCLE_COLOUR = (255, 0, 0)
ELLIPSE_COLOUR=(255,255,255)
BLACK = (0,0, 0)

 
def ellipse(xc,yc,rx,ry):
    x=0
    y=ry
    p1 = ry**2-(rx**2)*ry+0.25*(ry**2)
    dx=2*(ry**2)*x
    dy=2*(rx**2)*y
    while (dx<=dy):
        screen.set_at((x+xc,y+yc), ELLIPSE_COLOUR) 
        screen.set_at((-x+xc,y+yc), ELLIPSE_COLOUR) 
        screen.set_at((x+xc,-y+yc), ELLIPSE_COLOUR) 
        screen.set_at((-x+xc,-y+yc), ELLIPSE_COLOUR) 
        if p1<0:
            dx=2*(ry**2)*x
            dy=2*(rx**2)*y
            x+=1
            y=y
            p1=p1+dx+ry**2
        else:
            dx=2*(ry**2)*x
            dy=2*(rx**2)*y
            x+=1
            y-=1
            p1=p1+dx-dy+ry**2
    p2=ry**2*(x+0.5)**2+rx**2*(y-1)**2-(rx**2)*(ry**2)
    while(y!=0):
        screen.set_at((x+xc,y+yc), ELLIPSE_COLOUR) 
        screen.set_at((-x+xc,y+yc), ELLIPSE_COLOUR) 
        screen.set_at((x+xc,-y+yc), ELLIPSE_COLOUR) 
        screen.set_at((-x+xc,-y+yc), ELLIPSE_COLOUR) 
        if p2>0:
            dx=2*(ry**2)*x
            dy=2*(rx**2)*y
            x=x
            y-=1
            p2=p2-dy+rx**2
        else:
            dx=2*(ry**2)*x
            dy=2*(rx**2)*y
            x+=1
            y-=1
            p2=p2+dx-dy+rx**2
        
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a ellipse using midpoint ellipse algorithm
        ellipse(400,300,200,100)
      #  ellipse(400,300,350,200)
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()