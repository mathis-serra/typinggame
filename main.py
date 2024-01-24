import pygame
import sys
import random

# Initialize Pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


font = pygame.font.Font(None, 36)

# Set up variables
with open("word.txt", "r") as file:
    word_list = [line.strip() for line in file.readlines()]

current_word = random.choice(word_list)
input_text = ""
score = 0

# Set up game loop
clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_RETURN:
                if input_text == current_word:
                    score += 1
                    current_word = random.choice(word_list)
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Display current word
    word_surface = font.render(current_word, True, BLACK)
    word_rect = word_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(word_surface, word_rect)

    # Display input text
    input_surface = font.render(input_text, True, BLACK)
    input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(input_surface, input_rect)

    # Display score
    score_surface = font.render(f"Score: {score}", True, BLACK)
    score_rect = score_surface.get_rect(topleft=(10, 10))
    screen.blit(score_surface, score_rect)

    pygame.display.flip()
    clock.tick(30)  # Adjust the frame rate as needed
