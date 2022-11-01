import pygame
import random

# začátek hry
pygame.init()

# nastavení hry
player_speed = 8
aplle_speed = 2
score = 0
live = 5
aplle_speed_up = 0.2
aplle_speed_curent = aplle_speed
live_down = live
win_score = 10
# FTP a hodiny
clock = pygame.time.Clock()
FTP = 60

# vytvoření obrazovky
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moje hra")

# barvy
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
my_color = pygame.Color("#8bae33")

# nastavení textu
text_big = pygame.font.Font("font/moje.ttf", 50)
text_small = pygame.font.Font("font/moje.ttf", 30)

name_game_text = text_big.render("Sber ovoce", True, my_color)
name_game_text_rec = name_game_text.get_rect()
name_game_text_rec.centerx = width//2
name_game_text_rec.centery = 30

game_over = text_big.render("Konec hry Prohral jsi", True, my_color)
game_over_rec = game_over.get_rect()
game_over_rec.center = (width//2, height//2)

game_continue = text_big.render("Chces pokracovat stiskni jakoukoliv klavesu", True, my_color)
game_continue_rec = game_continue.get_rect()
game_continue_rec.center = (width//2, height//2 + 40)

game_win = text_big.render("Vyhral jsi pohar", True, my_color)
game_win_rec = game_win.get_rect()
game_win_rec.center = (width//2, height//2)

# nastavení obrázků
basket = pygame.image.load("img/shopping-cart-icon.png")
basket_image = basket.get_rect()
basket_image.center = (width//2, 450)

aplle = pygame.image.load("img/Apple-icon.png")
aplle_image = aplle.get_rect()
aplle_image.x = random.randint(0, width - 24)
aplle_image.y = -24

cup = pygame.image.load("img/cup-icon.png")
cup_image = cup.get_rect()
cup_image.center = (width//2, height//2 - 60)

# nastavení zvuků
pygame.mixer.music.load("sound/typatone.wav")
pygame.mixer.music.play(-1, 0.0)

loose = pygame.mixer.Sound("sound/lose.wav")
loose.set_volume(0.5)

pick = pygame.mixer.Sound("sound/pike.wav")
pick.set_volume(0.5)

# hlavní cyklus
let_continue = True
while let_continue:
    for event in pygame.event.get():
        if event.type == 256:
            let_continue = False

    # pohyb kláves s košíkem
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and basket_image.left > 0:
        basket_image.x -= player_speed
    elif key[pygame.K_RIGHT] and basket_image.right < width:
        basket_image.x += player_speed

    # pohyb jablka
    if aplle_image.y > 500:
        live_down -= 1
        loose.play()
        aplle_image.y = -24
        aplle_image.x = random.randint(0, width - 24)
    else:
        aplle_image.y += aplle_speed_curent

    # zachytávání kolize
    if basket_image.colliderect(aplle_image):
        score += 1
        aplle_speed_curent += aplle_speed_up
        aplle_image.x = random.randint(0, width - 24)
        aplle_image.y = -24
        pick.play()

    screen.fill(black)

    # tvary
    pygame.draw.line(screen, my_color, (0, 55), (width, 55), 3)

    # texty
    score_text = text_small.render(f"Skore: {score}", True, my_color)
    score_text_rec = score_text.get_rect()
    score_text_rec.left = 20

    live_image = text_small.render(f"zivoty: {live_down}", True, my_color)
    live_image_rec = live_image.get_rect()
    live_image_rec.right = width - 20

    # zobrazení textu
    screen.blit(name_game_text, name_game_text_rec)
    screen.blit(score_text, score_text_rec)
    screen.blit(live_image, live_image_rec)

    # zobrazení obrázků
    screen.blit(basket, basket_image)
    screen.blit(aplle, aplle_image)

    # kontrola výhry
    if score == win_score:
        screen.blit(game_win, game_win_rec)
        screen.blit(cup, cup_image)
        screen.blit(game_continue, game_continue_rec)
        pygame.mixer.music.stop()
        pygame.display.update()
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    live_down = live
                    aplle_speed_curent = aplle_speed
                    aplle_image.x = random.randint(0, width - 24)
                    aplle_image.y = - 24
                    basket_image.center = (width / 2, 450)
                    pygame.mixer.music.play()
                    pause = False
                elif event.type == pygame.QUIT:
                    pause = False
                    let_continue = False

    # kontrola konce hry
    if live_down == 0:
        screen.blit(game_over, game_over_rec)
        screen.blit(game_continue, game_continue_rec)
        pygame.mixer.music.stop()
        pygame.display.update()
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    live_down = live
                    aplle_speed_curent = aplle_speed
                    aplle_image.x = random.randint(0, width - 24)
                    aplle_image.y = - 24
                    basket_image.center = (width / 2, 450)
                    pygame.mixer.music.play()
                    pause = False
                elif event.type == pygame.QUIT:
                    pause = False
                    let_continue = False

    # obnovení obrazovky
    pygame.display.update()

    # zpomalení
    clock.tick(FTP)

# konec hry
pygame.quit()