#button_notes


import pygame

# class Button():
#     def __init__(self, color, x ,y ,width ,height , text=''):
#         self.color = color
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.text = text

#     def draw(self,win,outline=None):
#         #Call this method to draw the button on the screen
#         if outline:
#             pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
#         pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
#         if self.text != '':
#             font = pygame.font.SysFont('comicsans', 60)
#             text = font.render(self.text, 1, (0,0,0))
#             win.blit(text, [(self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2))])

#     def isOver(self, pos):
#         #Pos is the mouse position or a tuple of (x,y) coordinates
#         if pos[0] > self.x and pos[0] < self.x + self.width:
#             if pos[1] > self.y and pos[1] < self.y + self.height:
#                 return True
            
#         return False

class Button:

    def __init__(self, screen, color, x ,y ,width ,height , text=''):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text


    def display_text(self):    
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(self.text, 4, (215, 224, 236))
        self.screen.blit(text, [self.x+(self.width/2 - text.get_width()/2),  self.y+(self.height/2 - text.get_height()/2)])

    def draw(self):
        co_or = (self.x, self.y, self.width, self.height)
        co_ord = (self.x-7, self.y-7, self.width+15, self.height+15)

        pygame.draw.rect(self.screen, (0,0,0), co_ord)
        pygame.draw.rect(self.screen, self.color, co_or)
        # pygame.draw.arc(self.screen, self.color, co_or, 30.6, 15.3)
        self.display_text()
        
    def click_b(self, event, pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pos[0] > self.x and pos[0] < self.x + self.width) and (pos[1] > self.y and pos[1] < self.y + self.height) :        
                print("this was clicked")
    
# screen, colour, x, y, width, height

    def isOver(self, pos):
        self.draw()
        if (pos[0] > self.x and pos[0] < self.x + self.width) and (pos[1] > self.y and pos[1] < self.y + self.height) :
            # if pos[0] > self.x and pos[1] < self.y + self.height:
            pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, self.width, self.height))
            self.display_text()

        # else:
        #     pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        #     self.display_text()  

        # if (self.x + self.width) > self.x and (self.y + self.height) > pos[1] > self.y:
        #     pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, self.width, self.height))
        #     self.display_text()
        # else:
        #     pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        #     self.display_text()





# pygame.draw.rect(screen,BLUE,(200,150,100,50))
# font = pygame.font.SysFont('comicsans', 60)
# text = font.render("hello", 1, (0,0,0))
# screen.blit(text, [200, 150])



#pygame.draw.rect(screen, (0,0,0), (150,255,250,100),0)
#pygame.draw.polygon(screen, (0,255,0))




    # def isOver(self, pos):
    #     if (pos[0] > self.x and pos[0] < self.x + self.width) and (pos[1] > self.y and pos[1] < self.y + self.height) :
    #         # if pos[0] > self.x and pos[1] < self.y + self.height:
    #         pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, self.width, self.height))
    #         self.display_text()
    #     else:
    #         pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    #         self.display_text()  


    # def isOver(self, pos):
    #     if (pos[0] > self.x and pos[0] < self.x + self.width):
    #         if pos[0] > self.x and pos[1] < self.y + self.height:
    #             pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, self.width, self.height))
    #             self.display_text()
    #     else:
    #         pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    #         self.display_text() 