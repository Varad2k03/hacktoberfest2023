import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Collector")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


clock = pygame.time.Clock()


cart_width, cart_height = 80, 80
object_width, object_height = 50, 50
cart_x, cart_y = WIDTH // 2, HEIGHT - 100
object_x, object_y = random.randint(0, WIDTH - object_width), -object_height
score = 0
fall_counter = 0

object_shapes = [1, 2, 3]
object_shape = random.choice(object_shapes)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and cart_x > 0:
        cart_x -= 5
    if keys[pygame.K_RIGHT] and cart_x < WIDTH - cart_width:
        cart_x += 5

    object_y += 5
    if object_y > HEIGHT:
        object_y = -object_height
        object_x = random.randint(0, WIDTH - object_width)
        object_shape = random.choice(object_shapes)
        fall_counter += 1

        if fall_counter == 3:
            font = pygame.font.Font(None, 50)
            game_over_text = font.render("Game Over!", True, BLACK)
            score_text = font.render(f"Score: {score}", True, BLACK)
            WINDOW.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 50))
            WINDOW.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 50))
            pygame.display.update()
            pygame.time.wait(3000)  # Wait for 3 seconds
            pygame.quit()
            sys.exit()

   
    if cart_x < object_x + object_width and \
            cart_x + cart_width > object_x and \
            cart_y < object_y + object_height and \
            cart_y + cart_height > object_y:
        score += 1
        object_y = -object_height
        object_x = random.randint(0, WIDTH - object_width)
        object_shape = random.choice(object_shapes)

    # Draw everything
    WINDOW.fill(WHITE)

    pygame.draw.rect(WINDOW, BLACK, (cart_x, cart_y, cart_width, cart_height))

    if object_shape == 1:
        pygame.draw.rect(WINDOW, RED, (object_x, object_y, object_width, object_height))
    elif object_shape == 2:
        pygame.draw.rect(WINDOW, RED, (object_x, object_y, object_width, object_height // 2))
    elif object_shape == 3:
        pygame.draw.polygon(WINDOW, RED, [(object_x, object_y + object_height),
                                         (object_x + object_width, object_y + object_height),
                                         (object_x + (object_width // 2), object_y)])

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    fall_counter_text = font.render(f"Falls: {fall_counter}/3", True, BLACK)
    WINDOW.blit(score_text, (10, 10))
    WINDOW.blit(fall_counter_text, (10, 50))

    pygame.display.update()
    clock.tick(60)
