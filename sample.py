# pygameをimportしたら、必ず初期化を行う pygame.init()
import pygame

pygame.init()

# 画面を作成する

screen = pygame.display.set_mode((800, 600))
# 背景の色を変更する
screen.fill((150, 150, 150))
# Windowのタイトルを変更する
pygame.display.set_caption("Invaders Game")

# 画像の表示
img = pygame.image.load("player.png")


# 画面をずっと表示させる 無限ループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
# screen上を書き換えた場合、updateする必要がある
    pygame.display.update()