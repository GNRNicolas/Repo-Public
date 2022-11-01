import random
import sys
import pygame

"""pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()"""


"""while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                print('UP')
            if event.key == pygame.K_DOWN:
                print('DOWN')
            if event.key == pygame.K_RIGHT:
                print('RIGHT')
            if event.key == pygame.K_LEFT:
                print('LEFT')"""

"""red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = [red, green, blue]
    screen.fill(color)
    pygame.display.update()
    clock.tick(1)"""


"""x = 0
    y = 0
    for i in range(0,30):
        for j in range(0,30):

            x = 20*i
            y = 40*j + (i%2)*20

            width = 20
            height = 20
            rect = [x, y, width, height]
            red = 255
            green = 255
            blue = 255
            color = [red, green, blue]
            pygame.draw.rect(screen, color, rect)

    pygame.display.update()"""
    
"""snake = [50,50,20,60]
    black = [0,0,0]
    white = [255,255,255]
    color = black
    screen.fill(white)
    pygame.draw.rect(screen, color,snake)
    pygame.display.update()"""


white = [255, 255, 255]
black = [0, 0, 0]

snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]

pygame.init()
screen = pygame.display.set_mode([20*30, 20*30])
clock = pygame.time.Clock()
screen.fill(white)

"""for x, y in snake:
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, black, rect)"""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT :
                screen.fill(white)
                snake[0][0] = snake[1][0]
                snake[1][0] = snake[2][0]
                snake[2][0] = snake[2][0]+1
                for x, y in snake:
                    rect = [x*20, y*20, 20, 20]
                    pygame.draw.rect(screen, black, rect)
            if event.key == pygame.K_LEFT :
                screen.fill(white)
                snake[0][0] = snake[1][0]
                snake[1][0] = snake[2][0]
                snake[2][0] = snake[2][0]-1
                for x, y in snake:
                    rect = [x*20, y*20, 20, 20]
                    pygame.draw.rect(screen, black, rect)
            if event.key == pygame.K_UP :
                screen.fill(white)
                snake[0][1] = snake[1][1]
                snake[1][1] = snake[2][1]
                snake[2][1] = snake[2][1]-1
                for x, y in snake:
                    rect = [x*20, y*20, 20, 20]
                    pygame.draw.rect(screen, black, rect)           
            if event.key == pygame.K_DOWN :
                screen.fill(white)
                snake[0][1] = snake[1][1]
                snake[1][1] = snake[2][1]
                snake[2][1] = snake[2][1]+1
                for x, y in snake:
                    rect = [x*20, y*20, 20, 20]
                    pygame.draw.rect(screen, black, rect)           

    pygame.display.update()
    clock.tick(10)
