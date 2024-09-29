import pygame
import sys  # Import sys for system exit
from pygame.locals import *
import random
import os

NONE = 0
LEFT = 1
MID = 2
RIGHT = 3

clock = pygame.time.Clock()
FPS = 60
clock.tick(FPS)

locations = [LEFT, MID, RIGHT]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.font.init()
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)


def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Intro Scene Function
def intro_scene():
    intro = True
    Background = pygame.image.load("images/background.png")
    Background = pygame.transform.scale(Background, (1280, 720))
    WantedPoster = pygame.image.load("images/WantedPoster/WantedPoster_0.png")
    WantedPoster = pygame.transform.scale(WantedPoster, (648,704))
    
    ShootHimDead = pygame.image.load("images/WantedPoster/pixil-frame-0 3.png")
    ShootHimDead = pygame.transform.scale(ShootHimDead, (525, 550))
    
    Instructions = pygame.image.load("images/WantedPoster/pixil-frame-0 4.png")
    Instructions = pygame.transform.scale(Instructions, (230, 230))
    
    Instruction5 = pygame.image.load("images/WantedPoster/pixil-frame-0 5.png")
    Instruction5 = pygame.transform.scale(Instruction5, (230, 230))

    WantedMan = pygame.image.load("images/EnemyShoots/enemyshoots_00.png")
    WantedMan = pygame.transform.scale(WantedMan, (400, 400))

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.type != pygame.K_ESCAPE:  # Exit intro on keypress
                intro = False
         #add image for intro
        screen.fill(BLACK)
        screen.blit(Background, (0,0))
        screen.blit(WantedPoster, ((screen.get_width() - 648)/2,0))
        screen.blit(ShootHimDead, ((screen.get_width() - 648)/2 + 100, 335))
        screen.blit(Instructions, ((screen.get_width() - 648)/2 + 40, 160))
        screen.blit(WantedMan, ((screen.get_width() - 648)/2 + 225, 75))
        screen.blit(Instruction5, ((screen.get_width() - 648)/2 + 40, 305))
        
        # display_text("Welcome to the Wild Wild West!", font, BLACK, 120, 200)
        # display_text("Hide from the bad cowboy behind barrels and guess where he's hidden by clicking on the barrel you think he's hiding behind to shoot!", font, BLACK, 200, 400)
        # display_text("Do your best to evade his shots, you only have three lives!", font, BLACK, 300, 600)
        # display_text("Press A and D or Left arrow and Right arrow keys to roll behind any barrel", font, BLACK, 400, 800)
        # display_text("Press any key to continue...", font, BLACK, 500, 1000)
        pygame.display.flip()


def roll_right(begin, end):
    i = 0
    num_frames = len(os.listdir("images/RollRight"))
    distance = end[0][0] - begin[0][0]
    for frame in os.listdir("images/RollRight"):
        run_background()
        clock.tick(10)
        image = pygame.image.load("images/RollRight/"+frame)
        image = pygame.transform.scale(image, (250,250))
        screen.blit(image, (begin[0][0] + i - 20, avg_hero_height - 70))
        pygame.display.flip()
        i += distance/num_frames
    clock.tick(FPS)

def roll_left(begin, end):
    i = 0
    num_frames = len(os.listdir("images/RollLeft"))
    distance = end[0][0] - begin[0][0]
    for frame in os.listdir("images/RollLeft"):
        run_background()
        clock.tick(10)
        image = pygame.image.load("images/RollLeft/"+frame)
        image = pygame.transform.scale(image, (250,250))
        screen.blit(image, (begin[0][0] - 65 + i, avg_hero_height - 70))
        pygame.display.flip()
        i += distance/num_frames
    clock.tick(FPS)

def shoot_enemy(hero_pos, enemy_pos):
    height = 0
    for frame in os.listdir("images/HeroJump"):
        run_background()
        clock.tick(12)
        image = pygame.image.load("images/HeroJump/"+frame)
        image = pygame.transform.scale(image, (200,200))
        screen.blit(image, (hero_pos[0][0], hero_pos[0][1] - 100 - height))
        pygame.display.flip()
        height += 100

    hero_shooting_list = []
    for frame in os.listdir("images/HeroShooting"):
        hero_shooting_list.append(frame)
    enemy_shooting_list = []
    for frame in os.listdir("images/EnemyShoots"):
        enemy_shooting_list.append(frame)
    for i in range(len(hero_shooting_list)):
        run_background()
        clock.tick(12)
        hero_image = pygame.image.load("images/HeroShooting/"+ hero_shooting_list[i])
        hero_image = pygame.transform.scale(hero_image, (200,200))
        screen.blit(hero_image, (hero_pos[0][0], hero_pos[0][1] - 100 - height))
        enemy_image = pygame.image.load("images/EnemyShoots/"+ enemy_shooting_list[i])
        enemy_image = pygame.transform.scale(enemy_image, (150,150))
        screen.blit(enemy_image, (enemy_pos[0][0], enemy_pos[0][1] - 250))
        pygame.display.flip()

    final_enemy = pygame.image.load("images/EnemyShoots/" + enemy_shooting_list[len(enemy_shooting_list) - 1])
    final_enemy = pygame.transform.scale(final_enemy, (150,150))
    final_hero = pygame.image.load("images/HeroShooting/" + hero_shooting_list[len(hero_shooting_list) - 1])
    final_hero = pygame.transform.scale(final_hero, (200,200))

    for frame in os.listdir("Images/explosion"):
        run_background() #prob need to run characters at their top positions
        clock.tick(12)
        explosion_image = pygame.image.load("images/explosion/" + frame)
        explosion_image = pygame.transform.scale(explosion_image, (200,200))
        
        screen.blit(final_enemy, (enemy_pos[0][0], enemy_pos[0][1] - 250))
        
        screen.blit(final_hero, (hero_pos[0][0], hero_pos[0][1] - 100 - height))

        if hero_shot == LEFT:
            screen.blit(explosion_image, (enemy_barrel_left[0][0] - 20, enemy_barrel_left[0][1] - 240))
        elif hero_shot == MID:
            screen.blit(explosion_image, (enemy_barrel_mid[0][0] - 20, enemy_barrel_mid[0][1] - 240))
        elif hero_shot == RIGHT:
            screen.blit(explosion_image, (enemy_barrel_right[0][0] - 20, enemy_barrel_right[0][1] - 240))
        
        if enemy_shot == LEFT:
            screen.blit(explosion_image, (hero_barrel_left[0][0], hero_barrel_left[0][1] - 250))
        elif enemy_shot == MID:
            screen.blit(explosion_image, (hero_barrel_mid[0][0], hero_barrel_mid[0][1] - 250))
        elif enemy_shot == RIGHT:
            screen.blit(explosion_image, (hero_barrel_right[0][0], hero_barrel_right[0][1] - 250))
        pygame.display.flip()
    clock.tick(FPS)

def hero_death():
    for frame in os.listdir("images/HeroDeath"):
        run_background()
        clock.tick(7)
        image = pygame.image.load("images/HeroDeath/"+frame)
        image = pygame.transform.scale(image, (200, 200))
        if (hero_hiding_spot == LEFT):
            screen.blit(image, (hero_barrel_left[0][0] - 35, hero_barrel_left[0][1] - 170))
        elif (hero_hiding_spot == MID):
            screen.blit(image, (hero_barrel_mid[0][0] - 28, hero_barrel_mid[0][1] - 170))
        elif (hero_hiding_spot == RIGHT):
            screen.blit(image, (hero_barrel_right[0][0] - 20, hero_barrel_right[0][1] - 170))
        pygame.display.flip()

def enemy_death():
     for frame in os.listdir("images/EnemyDeath"):
        run_background()
        clock.tick(7)
        image = pygame.image.load("images/EnemyDeath/"+frame)
        image = pygame.transform.scale(image, (200, 200))
        if (enemy_hiding_spot == LEFT):
            screen.blit(image, (enemy_barrel_left[0][0] - 15, enemy_barrel_left[0][1] - 170))
        elif (enemy_hiding_spot == MID):
            screen.blit(image, (enemy_barrel_mid[0][0] - 8, enemy_barrel_mid[0][1] - 170))
        elif (enemy_hiding_spot == RIGHT):
            screen.blit(image, (enemy_barrel_right[0][0], enemy_barrel_right[0][1] - 170))
        pygame.display.flip()
        
def run_background():
    screen.fill("black")
    screen.blit(WildWestBackground, (0, 0))  # Blit at top-left corner
    
    screen.blit(EnemyBarrel, EnemyBarrelMidPos)
    screen.blit(EnemyBarrel, (EnemyBarrelMidPos[0] + EnemyBarrelOffset, EnemyBarrelMidPos[1]))  
    screen.blit(EnemyBarrel, (EnemyBarrelMidPos[0] - EnemyBarrelOffset, EnemyBarrelMidPos[1]))  

    HeroBarrelHeight = 425 #TODO make dynamic with changing window size
    HeroBarrelMidPos = (screen.get_width()/2-HeroBarrelSize[0]/2, HeroBarrelHeight)
    HeroBarrelOffset = 240 #TODO make dynamic with changing window size

    screen.blit(HeroBarrel, HeroBarrelMidPos)
    screen.blit(HeroBarrel, (HeroBarrelMidPos[0] + HeroBarrelOffset, HeroBarrelMidPos[1]))
    screen.blit(HeroBarrel, (HeroBarrelMidPos[0] - HeroBarrelOffset, HeroBarrelMidPos[1]))

    heart_offset = 55
    if enemy_health == 0:
        screen.blit(BlackHeart, (screen.get_width() -150, -30))
        screen.blit(BlackHeart, (screen.get_width() -150 - heart_offset, -30)) 
        screen.blit(BlackHeart, (screen.get_width() -150 - 2*heart_offset, -30))
    elif enemy_health == 1:
        screen.blit(RedHeart, (screen.get_width() -150, -30))
        screen.blit(BlackHeart, (screen.get_width() -150 - heart_offset, -30)) 
        screen.blit(BlackHeart, (screen.get_width() -150 - 2*heart_offset, -30))
    elif enemy_health == 2:
        screen.blit(RedHeart, (screen.get_width() -150, -30))
        screen.blit(RedHeart, (screen.get_width() -150 - heart_offset, -30)) 
        screen.blit(BlackHeart, (screen.get_width() -150 - 2*heart_offset, -30))
    elif enemy_health == 3:
        screen.blit(RedHeart, (screen.get_width() -150, -30))
        screen.blit(RedHeart, (screen.get_width() -150 - heart_offset, -30)) 
        screen.blit(RedHeart, (screen.get_width() -150 - 2*heart_offset, -30))

    if hero_health == 0:
        screen.blit(BlackHeart, (screen.get_width() -150, screen.get_height() - 180))
        screen.blit(BlackHeart, (screen.get_width() -150 - heart_offset, screen.get_height() - 180))
        screen.blit(BlackHeart, (screen.get_width() -150 - 2*heart_offset, screen.get_height() - 180))
    elif hero_health == 1:
        screen.blit(RedHeart, (screen.get_width() -150, screen.get_height() - 180))
        screen.blit(BlackHeart, (screen.get_width() -150 - heart_offset, screen.get_height() - 180))
        screen.blit(BlackHeart, (screen.get_width() -150 - 2*heart_offset, screen.get_height() - 180))
    elif hero_health == 2:
        screen.blit(RedHeart, (screen.get_width() -150, screen.get_height() - 180))
        screen.blit(RedHeart, (screen.get_width() -150 - heart_offset, screen.get_height() - 180))
        screen.blit(BlackHeart, (screen.get_width() -150 - 2*heart_offset, screen.get_height() - 180))
    elif hero_health == 3:
        screen.blit(RedHeart, (screen.get_width() -150, screen.get_height() - 180))
        screen.blit(RedHeart, (screen.get_width() -150 - heart_offset, screen.get_height() - 180))
        screen.blit(RedHeart, (screen.get_width() -150 - 2*heart_offset, screen.get_height() - 180))


pygame.init()

# Set up display
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)  #TODO set dimensions based on background
pygame.display.set_caption("Wild West Showdown")

# x and y ratio for positions (curr_pos / original_pos) 

#barrels [(x_start, y_start), (x_end, y_end)]
enemy_barrel_left = [(463,439),(533,349)]   #TODO set locations based on background dimensions
enemy_barrel_mid = [(602,439),(674,349)]
enemy_barrel_right = [(742,439),(813,349)]
hero_barrel_left = [(328,650),(464,475)]
hero_barrel_mid = [(568,650),(705,475)]
hero_barrel_right = [(809,650),(944,475)]

avg_hero_height = (hero_barrel_left[0][1] + hero_barrel_left[1][1])/2
enemy_hidden_pos = NONE

# Load images

try:
    WildWestBackground = pygame.image.load("images/background.png")
    Barrel = pygame.image.load("images/Barrels/Barrel_0.png")
    HighlightedBarrel = pygame.image.load("images/Barrels/highlightB_0.png")
    RedHeart = pygame.image.load("images/hearts/heart_0.png")
    BlackHeart = pygame.image.load("images/hearts/heart_1.png")
    IdleHero = pygame.image.load("images/HeroShooting/shootbullethero_4.png")
    BulletForward = pygame.image.load("images/shootbullethero_8.png")

    HeroBarrelSize = (250, 250)
    EnemyBarrelSize = (130, 130)
    HeroBarrel = pygame.transform.scale(Barrel, HeroBarrelSize)
    HeroHighlightedBarrel = pygame.transform.scale(HighlightedBarrel, HeroBarrelSize)
    EnemyBarrel = pygame.transform.scale(Barrel, EnemyBarrelSize)
    EnemyHighlightedBarrel = pygame.transform.scale(HighlightedBarrel, (135, 135))
    RedHeart = pygame.transform.scale(RedHeart, (180, 180))
    BlackHeart = pygame.transform.scale(BlackHeart, (180, 180))
    IdleHero = pygame.transform.scale(IdleHero, (200,200))
    BulletForward = pygame.transform.scale(BulletForward, (60,60))
    BulletBackward = pygame.transform.rotate(BulletForward, 180)
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

enemy_selected = False #TODO implement hovering over the enemy barrel

hero_shot = NONE
hero_hiding_spot = MID

enemy_shot = NONE
enemy_hiding_spot = NONE

hero_health = 3 #set at 3 to start
enemy_health = 3

# rectLeft = EnemyBarrel.get_rect()
rectLeft = EnemyBarrel.get_rect()
# rectLeft.height = enemy_barrel_left[1][0] - enemy_barrel_left[1][1]
#pygame.Rect((enemy_barrel_left[1]), (enemy_barrel_left[1][0] - enemy_barrel_left[0][0], enemy_barrel_left[1][1] - enemy_barrel_left[0][1]))
rectLeft.bottomleft = (464,460)
rectLeft.width = 73
rectLeft.height = 92

rectMid = EnemyBarrel.get_rect()
rectMid.bottomleft = (602,460)
rectMid.width = 73
rectMid.height = 92

rectRight = EnemyBarrel.get_rect()
rectRight.bottomleft = (742,460)
rectRight.width = 73
rectRight.height = 92

EnemyBarrelHeight = 325
EnemyBarrelOffset = 140
EnemyBarrelMidPos = (screen.get_width()/2 - EnemyBarrelSize[0]/2, EnemyBarrelHeight)

game_over = False
running = True

intro_scene()

# Main game loop

while running:
    # Handle events

    if not game_over:
        WildWestBackground = pygame.transform.scale(WildWestBackground, (screen.get_width(), screen.get_height()))

        
        mouse_pos = pygame.mouse.get_pos()  #.set to set original position if needed
        mx = mouse_pos[0]
        my = mouse_pos[1]

        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Ensure the program exits completely

            enemy_hiding_spot = random.choice(locations)
            enemy_shot = random.choice(locations)

            if enemy_hiding_spot == LEFT:
                enemy_hidden_pos = enemy_barrel_left
            elif enemy_hiding_spot == MID:
                enemy_hidden_pos = enemy_barrel_mid
            elif enemy_hiding_spot == RIGHT:
                enemy_hidden_pos = enemy_barrel_right

            hero_shot = NONE
            if not enemy_selected:
                
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1: #left click #actually selecting the enemy barrel
                        if (enemy_barrel_left[0][0] <= mx <= enemy_barrel_left[1][0] and enemy_barrel_left[0][1] >= my >= enemy_barrel_left[1][1]):
                            hero_shot = LEFT
                            enemy_selected = True
                        elif (enemy_barrel_mid[0][0] <= mx <= enemy_barrel_mid[1][0] and enemy_barrel_mid[0][1] >= my >= enemy_barrel_mid[1][1]):
                            hero_shot = MID
                            enemy_selected = True
                        elif (enemy_barrel_right[0][0] <= mx <= enemy_barrel_right[1][0] and enemy_barrel_right[0][1] >= my >= enemy_barrel_right[1][1]):
                            hero_shot = RIGHT
                            enemy_selected = True
                        else:
                            enemy_selected = False
                        
                        if enemy_selected:
                            if hero_hiding_spot == LEFT:
                                shoot_enemy(hero_barrel_left, enemy_hidden_pos)
                                
                            elif hero_hiding_spot == MID:
                                shoot_enemy(hero_barrel_mid, enemy_hidden_pos)
                                
                            elif hero_hiding_spot == RIGHT:
                                shoot_enemy(hero_barrel_right, enemy_hidden_pos)
                                

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_d or event.key == K_RIGHT:
                        if hero_hiding_spot == LEFT:
                            hero_hiding_spot = MID
                            roll_right(hero_barrel_left, hero_barrel_mid)
                        elif hero_hiding_spot == MID:
                            hero_hiding_spot = RIGHT
                            roll_right(hero_barrel_mid, hero_barrel_right)
                    if event.key == K_a or event.key == K_LEFT:
                        if hero_hiding_spot == MID:
                            hero_hiding_spot = LEFT
                            roll_left(hero_barrel_mid, hero_barrel_left)    
                        elif hero_hiding_spot == RIGHT:
                            hero_hiding_spot = MID
                            roll_left(hero_barrel_right, hero_barrel_mid)
                #random generate enemy_hiding_location and enemy_shot
                #fire shot from hero_hding_spot to enemy_selected
                #fire shot from enemy_hiding_spot to enemy_shot
                #show hit effect on selected target
            if (hero_shot == enemy_hiding_spot and hero_shot != NONE):
                enemy_health -= 1
                hero_shot = NONE
                if enemy_health == 0:
                    enemy_death()
                    game_over = True
                    break
            if (enemy_shot == hero_hiding_spot and enemy_selected):
                hero_health -= 1
                if hero_health == 0:
                    hero_death()
                    game_over = True
                    break
            enemy_shot = NONE
            hero_shot = NONE
            if enemy_selected:
                enemy_selected = False
                    
        # Draw background image
        run_background()

        if rectLeft.collidepoint(mouse_pos):
            screen.blit(EnemyHighlightedBarrel, (EnemyBarrelMidPos[0] - EnemyBarrelOffset - 3, EnemyBarrelMidPos[1]))
        elif rectMid.collidepoint(mouse_pos):
            screen.blit(EnemyHighlightedBarrel, (EnemyBarrelMidPos[0] - 3, EnemyBarrelMidPos[1]))
        elif rectRight.collidepoint(mouse_pos):
            screen.blit(EnemyHighlightedBarrel, (EnemyBarrelMidPos[0] + EnemyBarrelOffset - 3, EnemyBarrelMidPos[1])) 
        
        if (hero_hiding_spot == LEFT):
                screen.blit(IdleHero, (hero_barrel_left[0][0] - 35, hero_barrel_left[0][1] - 170))
        elif (hero_hiding_spot == MID):
            screen.blit(IdleHero, (hero_barrel_mid[0][0] - 28, hero_barrel_mid[0][1] - 170))
        elif (hero_hiding_spot == RIGHT):
            screen.blit(IdleHero, (hero_barrel_right[0][0] - 20, hero_barrel_right[0][1] - 170))
        
        clock.tick(FPS)
        pygame.display.flip()

    else:

        if (hero_health > enemy_health):
            Win = pygame.image.load("images/StartEnd/blackWin_0.png")
            Win = pygame.transform.scale(Win, (1280, 720))
            screen.blit(Win, (0,0))
            pygame.display.flip()
        else:
            Lose = pygame.image.load("images/StartEnd/youLose_0.png")
            Lose = pygame.transform.scale(Lose, (1280, 720))
            screen.blit(Lose, (0,0))
            pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    enemy_selected = False
                    hero_shot = NONE
                    enemy_shot = NONE
                    hero_health = 3
                    enemy_health = 3
                    game_over = False
                
        
pygame.quit()
sys.exit()