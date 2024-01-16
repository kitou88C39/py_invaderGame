# pygameをimportしたら、必ず初期化を行う pygame.init()
import pygame
# 音声の出力
from pygame import mixer
import ramdom
import math

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

# インベーダーの配置
enemyImg = pygame.image.load("enemy.png")
enemyX = ramdom.randint(0, 736)
enemyY = amdom.randint(50, 150)
enemyX_change, enemyY_change = 4, 40

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX, bulletY = 0, 480
bulletX_change, bulletY_change = 0, 3
bullet_state = "ready"


# 音声の出力
# mixer.Sound("laser.wav").play()

#Score
score_value = 0

def player(x, y):
    screen.bulit(playerImg, (x, y))

def enemy(x, y):
    screen.bulit(enemyImg, (x, y))

# 弾の発射
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.bulit(bulletImg, (x + 16, y + 10))


# 敵と弾が衝突
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True #衝突
    else:
        return False #衝突していない


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


    # player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy
    if enemyY > 440:
        break
    enemyX += enemyX_change
    if enemyX <= 0: #左端に来たら
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4 #右端に来たら
        enemyY += enemyY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        enemyX = ramdom.randint(0, 736)
        enemyY = ramdom.randint(50, 150)
    enemy(enemyX, enemyY)


    #score
    font = pygame.font.SyFont(None, 32) #フォントの作成　Noneはデフォルトのfreessansbold.ttf
    score = font.render(f"Score : {str(score_value)}", True, (255,255,255)) #テキストを描画したら、surfaceの作成
    screen.blit(score, (20, 50))


    player(playerX, playerY)
    enemy(enemyX, enemyY)
# screen上を書き換えた場合、updateする必要がある
    pygame.display.update()