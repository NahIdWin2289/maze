from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.2)
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load("background.jpg"), (700, 500))
clock = time.Clock()
FPS = 60
font.init()
font1 = font.SysFont('Arial', 70)
game = True
mixer.music.play(-1)
kick_musik = mixer.Sound('kick.ogg')
kick_musik.set_volume(0.1)
money_musik = mixer.Sound('money.ogg')
money_musik.set_volume(0.1)
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size = (65, 65)):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - 65:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 65:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = 'Left'
    def update(self):
        if self.direction == 'Left':
             self.rect.x -= self.speed
        else:
             self.rect.x += self.speed
        if self.rect.x <= 420:
            self.direction = 'Right'
        elif self.rect.x >= 615:
            self.direction = 'Left'

gg = Player('hero.png', 0, 430, 8, (55, 55))
anto = Enemy('cyborg.png', 615, 275, 7)
gold = GameSprite('treasure.png', 530, 430, 0)
rapira = GameSprite('rapira.png', 40, 365, 0, (180, 40))
r2 = GameSprite('rapirazov.png', 195, 265, 0, (35, 140))
r3 = GameSprite('rapirazov.png', 310, 365, 0, (35, 140))
r4 = GameSprite('rapirazov.png', 315, 225, 0, (35, 140))
r5 = GameSprite('rapirazov.png', 320, 85, 0, (35, 140))
r6 =GameSprite('rapirazov.png', 200, 125, 0, (35, 140))
r7 = GameSprite('rapirazov.png', 200, 0, 0, (35, 140))
r8 = GameSprite('rapira.png', 320, 85, 0, (160, 30))
r9 = GameSprite('rapira.png', 460, 85, 0, (160, 30))
r10 = GameSprite('rapira.png', 320, 210, 0, (140, 30))
r11 = GameSprite('rapira.png', 560, 210, 0, (140, 30))
while game:
    window.blit(background, (0, 0))
    if finish == False:
        gg.reset()
        anto.reset()
        gold.reset()
        gg.update()
        anto.update()
        rapira.reset()
        r2.reset()
        r3.reset()
        r4.reset()
        r5.reset()
        r6.reset()
        r7.reset()
        r8.reset()
        r9.reset()
        r10.reset()
        r11.reset()
        if sprite.collide_rect(gg, anto):
            kick_musik.play()
            finish = True
            win = font1.render('YOU LOSE', True, (255, 215, 0))
        if sprite.collide_rect(gg, gold):
            money_musik.play()
            finish = True
            win = font1.render('YOU WIN', True, (255, 215, 0))
        if sprite.collide_rect(gg, rapira) or sprite.collide_rect(gg, r2) or sprite.collide_rect(gg, r3) or sprite.collide_rect(gg, r4) or sprite.collide_rect(gg, r5) or sprite.collide_rect(gg, r6) or sprite.collide_rect(gg, r7) or sprite.collide_rect(gg, r8) or sprite.collide_rect(gg, r9) or sprite.collide_rect(gg, r10) or sprite.collide_rect(gg, r11):
            kick_musik.play()
            gg.rect.x = 0
            gg.rect.y = 430
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
             if e.key == K_SPACE and finish == True:
                finish = False
                gg.rect.x = 0
                gg.rect.y = 430
            
    if finish == True:
        window.blit(win, (220, 220))
        

    clock.tick(FPS)
    display.update()