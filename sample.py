# pygameをimportしたら、必ず初期化を行う pygame.init()
import pygame

pygame.init()

# 画面を作成する

screen = pygame.display.set_mode((800, 600))

# 画面をずっと表示させる

running = True
while running: