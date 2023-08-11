import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 1600, 1200
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 200
BALL_SIZE = 50
PADDLE_SPEED = 50
BALL_SPEED_X = 10
BALL_SPEED_Y = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Create paddles and ball
player_paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Game loop
running = True
clock = pygame.time.Clock()

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player paddle with mouse
    player_paddle.x, player_paddle.y = pygame.mouse.get_pos()
    player_paddle.x -= PADDLE_WIDTH // 2
    player_paddle.y -= PADDLE_HEIGHT // 2
    player_paddle.x = max(0, min(player_paddle.x, WIDTH - PADDLE_WIDTH))
    player_paddle.y = max(0, min(player_paddle.y, HEIGHT - PADDLE_HEIGHT))

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if check_collision(ball, player_paddle):
        ball_speed_x = -ball_speed_x  # Reverse the horizontal direction

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
