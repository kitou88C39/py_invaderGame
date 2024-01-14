# pygameをimportしたら、必ず初期化を行う pygame.init()
import pygame

pygame.init()

# 画面を作成する

screen = pygame.display.set_mode((800, 600))
# Windowのタイトルを変更する
pygame.display.set_caption("Invaders Game")



# 画面をずっと表示させる 無限ループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
# タイトルの変更