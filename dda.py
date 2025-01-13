import pygame

pygame.init()

width,height=800,600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("DDA Line Drawing Algorithm")

white=(255,255,255)
black=(0,0,0)

def dda_line(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1

    if abs(dx)>abs(dy):
        steps=abs(dx)
    else:
        steps=abs(dy)

    x_inc=dx/steps
    y_inc=dy/steps

    x,y=x1,y1

    for _ in range(steps):
        pygame.draw.circle(screen,black,(round(x),round(y)),1)#(surface,color,centre_of_circle,radius)
        x+=x_inc
        y+=y_inc

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill(white)

    dda_line(100,100,700,500)

    pygame.display.flip()

pygame.quit()