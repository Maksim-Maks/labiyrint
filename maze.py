import pygame

WIDTH = 1200
HEIGHT = 700
SIZE = (WIDTH,HEIGHT)

window = pygame.display.set_mode(SIZE)

background = pygame.transform.scale(
    pygame.image.load("background.jpg"),
    SIZE
)
FPS = 60
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image ,coords: tuple, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image),
        (65,65))
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.speed = speed

    def reset(self):
        window.blit(self.image, self.rect.topleft)


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed



class Enemy(GameSprite):
    direction = "left"
    def update(self, x1 , x2):
        if self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed
        
        if self.rect.x <= x1:
            self.direction = 'right'
        elif self.rect.x >= x2:
            self.direction = 'left'


class Wall(pygame.sprite.Sprite):
    def __init__(self,coords,size,color):
        self.rect = pygame.rect.Rect(coords,size)
        self.color = color
    def draw_wall(self):
        pygame.draw.rect(window,self.color, self.rect)





player = Player("hero.png", (40,HEIGHT-40), 5)
enemy = Enemy("cyborg.png",(WIDTH-100,HEIGHT/2), 5)
gold = GameSprite("treasure.png",(WIDTH-40, HEIGHT-60), 0)


walls = [ Wall((10,10),(WIDTH-100,10),(255,0,0)),
Wall((10,10),(10,HEIGHT-150),(255,0,0)),
Wall((10,HEIGHT-150),(200,10),(255,0,0)),
Wall((300,HEIGHT-150),(700,10),(255,0,0)),
Wall((495,HEIGHT-150),(10,500),(255,0,0)),
Wall((495,100),(10,HEIGHT),(255,0,0)),
Wall((595,100),(350,10),(255,0,0)),
Wall((500,250),(300,10),(255,0,0)),
Wall((100,95),(10,300),(255,0,0))
]




game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    window.blit(background,(0,0))
    player.update()
    player.reset()
    enemy.update(WIDTH/2, WIDTH)
    enemy.reset()
    gold.reset()

    for w in walls:
        w.draw_wall()
    

    pygame.display.update()
    clock.tick(FPS)