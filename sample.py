# pygameをimportしたら、必ず初期化を行う pygame.init()
import pygame
# 音声の出力
from pygame import mixer

pygame.init()

# 画面を作成する

screen = pygame.display.set_mode((800, 600))
# 背景の色を変更する
screen.fill((150, 150, 150))
# Windowのタイトルを変更する
pygame.display.set_caption("Invaders Game")

# 画像の表示
img = pygame.image.load("player.png")
X = 370
Y = 400

# 音声の出力
mixer.Sound("laser.wav").play()


# 画面をずっと表示させる 無限ループ
running = True
while running:
    # 画像の表示
    screen.bulit(img, (X,Y)) # bulit(オブジェクト, (X,Y)) ⇨ オブジェクトをX,Yに配置
    # 文字の表示
    font = pygame.font.System(None, 80)
    message = font.render("Hello world")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
# screen上を書き換えた場合、updateする必要がある
    pygame.display.update()