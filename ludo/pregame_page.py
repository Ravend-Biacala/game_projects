import pygame
import sys
import button
pygame.init()


blue = (12, 63, 186)
green = (0, 179, 0)
yellow = (179, 179, 0)
red =(242, 120, 107)

size = width, height = 1400, 800 
screen = pygame.display.set_mode(size)
image = pygame.image.load("background.jpg").convert()

screen.blit(image, [0, 0])

# screen, colour, x, y, width, height

heading = button.Button(screen, green, 535, 225, 320, 65, "Players Game")
player1 = button.Button(screen, red, 370, 370, 200, 50, "player1")
player2 = button.Button(screen, blue, 710, 370, 200, 50, "player2")
player3 = button.Button(screen, yellow, 370, 510, 200, 50, "player3")
player4 = button.Button(screen, green, 710, 510, 200, 50, "player4")

while True:
    pygame.display.update()
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    print(pos[0], pos[1])

    pygame.draw.rect(screen,(191, 191, 191),(350,200,700,450))
    heading.draw()
    player1.isOver(pos)
    player2.isOver(pos)
    player3.isOver(pos)
    player4.isOver(pos)


    



