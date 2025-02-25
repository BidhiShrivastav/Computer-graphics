import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 600
WHITE,PINK,GRAY, BLACK = (255, 255, 255), (255,209,220), (128,128,128), (0, 0, 0)
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
SPEED = 5

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Blocks")
clock = pygame.time.Clock()

# Load background image
background = pygame.image.load("background.png")
bg_y1 = 0
bg_y2 = -HEIGHT
bg_speed = 3  # Background scroll speed

# Player setup
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - 100
player_speed = 7

# Obstacles setup
obstacles = []
def create_obstacle():
    x = random.randint(0, WIDTH - OBSTACLE_SIZE)
    y = -OBSTACLE_SIZE
    obstacles.append([x, y])

def move_obstacles():
    for obstacle in obstacles:
        obstacle[1] += SPEED

    # Remove obstacles that go off-screen
    obstacles[:] = [obs for obs in obstacles if obs[1] < HEIGHT]

def check_collision():
    for obstacle in obstacles:
        if (player_x < obstacle[0] < player_x + PLAYER_SIZE or player_x < obstacle[0] + OBSTACLE_SIZE < player_x + PLAYER_SIZE) and \
           (player_y < obstacle[1] < player_y + PLAYER_SIZE or player_y < obstacle[1] + OBSTACLE_SIZE < player_y + PLAYER_SIZE):
            return True
    return False

# Game loop
running = True
while running:
    screen.fill(WHITE)
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move background for scrolling effect
    bg_y1 += bg_speed
    bg_y2 += bg_speed

    if bg_y1 >= HEIGHT:
        bg_y1 = -HEIGHT
    if bg_y2 >= HEIGHT:
        bg_y2 = -HEIGHT

    screen.blit(background, (0, bg_y1))
    screen.blit(background, (0, bg_y2))

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += player_speed

    # Spawn obstacles
    if random.randint(1, 30) == 1:
        create_obstacle()
    move_obstacles()

    # Draw player
    pygame.draw.rect(screen,GRAY, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    
    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen,PINK, (obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE))
    
    # Check for collision
    if check_collision():
        running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
