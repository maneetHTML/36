import pygame
import random
pygame.init()
width,height=500,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Colorful Bounce")
clock = pygame.time.Clock()
BG_Color = [pygame.Color("blue"),pygame.Color("black"),pygame.Color("white"),pygame.Color("lightgray"),pygame.Color("lightblue"),pygame.Color("Magenta")]
SPRITE_Color = [pygame.Color("yellow"),pygame.Color("red"),pygame.Color("orange")]
bg_color = random.choice(BG_Color)
CHANGE_SPRITE_Color=pygame.USEREVENT +1
CHANGE_BG_Color=pygame.USEREVENT +2
class Bouncer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30,20))
        self.image.fill(random.choice(SPRITE_Color))
        self.rect = self.image.get_rect(x=random.randint(0,width -30),y=random.randint(0,height -20))
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        hit = False
        if self.rect.left<=0 or self.rect.right>=width:
            self.velocity[0]*= -1
            hit=True
        if self.rect.top<=0 or self.rect.bottom>=height:
            self.velocity[0]*= -1
            hit=True
        if hit:
            pygame.event.post(pygame.event.Event(CHANGE_SPRITE_Color))
            pygame.event.post(pygame.event.Event(CHANGE_BG_Color))
    def change_color(self):
        self.image.fill(random.choice(SPRITE_Color))
sprite = Bouncer()
sprites = pygame.sprite.Group(sprite)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_SPRITE_Color:
            sprite.change_color()
        elif event.type == CHANGE_BG_Color:
            bg_color = random.choice(BG_Color)
    sprites.update()
    screen.fill(bg_color)
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()