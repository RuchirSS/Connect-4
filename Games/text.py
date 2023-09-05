import pygame

pygame.init()

cyan = (0, 255 , 255)
transparentCyan = (10,142,142)
color = transparentCyan

class Text:
    def __init__(self,msg,x,y,size):
        self.FONT = pygame.font.Font('Games\Assets\KeaniaOne-Regular.ttf',size)
        self.TEXT = msg
        self.TEXTSURFACE = self.FONT.render(self.TEXT,True,cyan)
        self.x = x
        self.y = y

    def print(self,surface): 
        surface.blit(self.TEXTSURFACE,(self.x,self.y))



     

