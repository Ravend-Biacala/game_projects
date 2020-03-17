import pygame

class Board:

    def __init__(self):
        self.display_size_x = 1800
        self.display_size_y = 1000
        self.gameDisplay = pygame.display.set_mode((self.display_size_x, self.display_size_y))

    def createBoard(self):
        '''create Ludo board'''
        pygame.display.set_caption("Ludo")
        self.gameDisplay.fill(BLUE_BACKGROUND)
        self.generateTiles()
        self.createTriangleHome()
        self.createBaseCircles()
        self.createTokens() 
        # border around board
        pygame.draw.rect(self.gameDisplay, BLACK, [self.size+self.boardOverall, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)
        pygame.display.update()