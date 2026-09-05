import pgzrun
import random

WIDTH = 1200
HEIGHT = 600
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
TITLE = 'Gallaga Game'

score = 0
lives = 3
is_game_over = False
speed = 5
bullets = []
enemies = []

#create the ship
ship = Actor('ship.png')
ship.pos = (CENTER_X , CENTER_Y - 60)

#create the enemies
for i in range(8):
    enemy = Actor('bug.png')
    enemy.x = random.randint(0,WIDTH - 80)
    enemy.y = random.randint(-100, 0)
    enemies.append(enemy)

def display_score():
    screen.draw.text(f'Score:{score}',(50,30))
    screen.draw.text(f'Lives:{lives}',(50,60))

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor('bullet.png')
        bullet.x = ship.x
        bullet.y = ship.y - 50
        bullets.append(bullet)

#function to draw game 
def draw():
    if lives > 0:
        screen.clear()
        screen.fill('dark blue')
        ship.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        display_score()
    else:
        game_over_screen()

#update the game state
def update():
    global score , lives
    #add movement to the ship
    if keyboard.left :
        ship.x -= speed 
        if ship.x <= 0 :
            ship.x = 0
    elif keyboard.right:
        ship.x += speed
        if ship >= WIDTH:
            ship.x = WIDTH
    #move the bullets
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    #move the enemies
    for enemy in enemies:
        enemy.y += 5
        if enemy.y >= HEIGHT:
            enemy.x = random.randint(0,WIDTH - 80)
            enemy.y = random.randint(-100,0)
        #check for collistion w/ bullets
        for bullet in bullets :
            if enemy.colliderect(bullet):
                score += 100
                sounds.eep.play()
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemies:
                    enemies.remove(enemy)
                break
        #check for collision with the ship
        if enemy.colliderect(ship):
            lives -= 1
            if enemy in enemies:
                enemies.remove(enemy)
            if lives == 0:
                game_over()
    # continuasly create new enemies
    if len(enemies)  < 8:
         enemy = Actor('bug.png')
         enemy.x = random.randint(0,WIDTH - 80)
         enemy.y = random.randint(-100, 0)
         enemies.append(enemy)

def game_over():
    global is_game_over
    is_game_over = True

def game_over_screen():
    screen.clear()
    screen.fill('#D90429')
    screen.draw.text(f'Game Over!!!',(CENTER_X - 150, CENTER_Y))


pgzrun.go()