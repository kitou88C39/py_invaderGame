# pygameをimportしたら、必ず初期化を行う pygame.init()
import pygame
# 音声の出力
from pygame import mixer

pygame.init()

# 画面を作成する

screen = pygame.display.set_mode((800, 600))
# 背景の色を変更する
# screen.fill((150, 150, 150))
# Windowのタイトルを変更する
pygame.display.set_caption("Invaders Game")

# Playerの配置
PlayerImg = pygame.image.load("player.png")
playerX, playerY = 370, 400
playerX_change = 0

# 音声の出力
# mixer.Sound("laser.wav").play()

def player(x, y):
    screen.bulit(playerImg, (x, y))


# 画面をずっと表示させる 無限ループ
running = True
while running:
    screen.fill((0, 0, 0))
    # 画像の表示
    # screen.bulit(img, (X,Y)) # bulit(オブジェクト, (X,Y)) ⇨ オブジェクトをX,Yに配置
    # 文字の表示
    # font = pygame.font.System(None, 80)
    # message = font.render("Hello world", False, (255, 255, 255))
    # screen.bulit(message, (20, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 矢印キーを動かして、playerを動かす
    if event.type == pygame.KEYDOWN:
       if event.type == pygame.K_LEFT:
            playerX_change = -1.5
       if event.type == pygame.K_RIGHT:
            playerX_change = 1.5
        # if event.type == pygame.K_SPACE:
            # if bullet_state is 'ready':
            #     bulletX = playerX
            #     fire_bullet(bulletX, bulletY)
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # playerX += 1.5
    playerX += playerX_change
    player(playerX, playerY)
# screen上を書き換えた場合、updateする必要がある
    pygame.display.update()