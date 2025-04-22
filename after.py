import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Bounce")
clock = pygame.time.Clock()

# Colors
BG_COLORS = [pygame.Color('yellow'), pygame.Color('magenta'), pygame.Color('orange'), pygame.Color('white')]
SPRITE_COLORS = [pygame.Color('blue'), pygame.Color('lightblue'), pygame.Color('darkblue')]
bg_color = random.choice(BG_COLORS)

# Custom events
CHANGE_SPRITE_COLOR = pygame.USEREVENT + 1
CHANGE_BG_COLOR = pygame.USEREVENT + 2

# Sprite class
class Bouncer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 20))
        self.image.fill(random.choice(SPRITE_COLORS))
        self.rect = self.image.get_rect(x=random.randint(0, WIDTH - 30), y=random.randint(0, HEIGHT - 20))
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        hit = False
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.velocity[0] *= -1
            hit = True
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.velocity[1] *= -1
            hit = True
        if hit:
            pygame.event.post(pygame.event.Event(CHANGE_SPRITE_COLOR))
            pygame.event.post(pygame.event.Event(CHANGE_BG_COLOR))

    def change_color(self):
        self.image.fill(random.choice(SPRITE_COLORS))

# Create sprite
sprite = Bouncer()
sprites = pygame.sprite.Group(sprite)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_SPRITE_COLOR:
            sprite.change_color()
        elif event.type == CHANGE_BG_COLOR:
            bg_color = random.choice(BG_COLORS)

    sprites.update()
    screen.fill(bg_color)
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(140)

pygame.quit()
