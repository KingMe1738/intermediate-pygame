# Only needed if you're running in GitHub Codespaces
import os
os.environ["DISPLAY"] = ":1"
import pygame

# Game settings
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
PADDLE_SPEED = 7
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Paddle positions
left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball position and velocity

ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_vel_x = BALL_SPEED_X
ball_vel_y = BALL_SPEED_Y

# Scores
left_score = 0
right_score = 0

# Font for score display
score_font = pygame.font.SysFont("Arial", 48)
winner_text_font = pygame.font.SysFont("Arial", 36)

def reset_ball():
    global ball, ball_vel_x, ball_vel_y
    ball.x = WIDTH // 2 - BALL_SIZE // 2
    ball.y = HEIGHT // 2 - BALL_SIZE // 2
    ball_vel_x *= -1
    ball_vel_y = BALL_SPEED_Y if ball_vel_y > 0 else -BALL_SPEED_Y

running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        # Left paddle controls (W/S)
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED
        # Right paddle controls (Up/Down)
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Ball movement
        ball.x += ball_vel_x
        ball.y += ball_vel_y

        # Ball collision with top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_vel_y *= -1

        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_vel_x *= -1

        # Ball out of bounds (score)
        if ball.left <= 0:
            right_score += 1
            reset_ball()
        elif ball.right >= WIDTH:
            left_score += 1
            reset_ball()

        # Check for winner
        if left_score >= 10 or right_score >= 10:
            game_over = True

    # Drawing
    # Colors
    BG_COLOR = (144, 238, 144)  # Light green
    LEFT_PADDLE_COLOR = (0, 0, 255)  # Blue
    RIGHT_PADDLE_COLOR = (255, 0, 0)  # Red
    BALL_COLOR = (255, 215, 0)  # Gold
    LINE_COLOR = (255, 255, 255)  # White


    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, LEFT_PADDLE_COLOR, left_paddle)
    pygame.draw.rect(screen, RIGHT_PADDLE_COLOR, right_paddle)
    pygame.draw.ellipse(screen, BALL_COLOR, ball)
    pygame.draw.aaline(screen, LINE_COLOR, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw scores
    left_score_surface = score_font.render(str(left_score), True, (0, 0, 0))
    right_score_surface = score_font.render(str(right_score), True, (0, 0, 0))
    screen.blit(left_score_surface, (WIDTH // 4 - left_score_surface.get_width() // 2, 20))
    screen.blit(right_score_surface, (3 * WIDTH // 4 - right_score_surface.get_width() // 2, 20))

    # Display winner/loser text if game over
    if game_over:
        if left_score >= 10:
            left_text = winner_text_font.render("Winner", True, (0, 128, 0))
            right_text = winner_text_font.render("Loser", True, (128, 0, 0))
        else:
            left_text = winner_text_font.render("Loser", True, (128, 0, 0))
            right_text = winner_text_font.render("Winner", True, (0, 128, 0))
        screen.blit(left_text, (WIDTH // 4 - left_text.get_width() // 2, 80))
        screen.blit(right_text, (3 * WIDTH // 4 - right_text.get_width() // 2, 80))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()