import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Circle")
# Colors
BLACK = (255, 255, 255)
PINK = (255, 192, 203)
TURQUOISE=(64,224,208)

# Game settings
circle_radius = 50
score = 0

# Font for displaying score
font = pygame.font.SysFont("Times New Roman", 20)

# Circle starting position
circle_x = random.randint(circle_radius, WIDTH - circle_radius)
circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

# Game loop
running = True
while running:

    screen.fill(TURQUOISE)
   

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the circle is clicked
            if (mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2 <= circle_radius ** 2:
                score += 1
                # Move the circle to a new random position
                circle_x = random.randint(circle_radius, WIDTH - circle_radius)
                circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

    # Draw the circle
    pygame.draw.circle(screen,PINK, (circle_x, circle_y), circle_radius)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (20, 50))

    # Update the display
    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
