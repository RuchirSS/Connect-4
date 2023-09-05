import pygame

pygame.init()

cyan = (0, 255 , 255)
transparentCyan = (10,142,142)
color = transparentCyan
class TextBox:
    def __init__(self,x,y,l,b) :
        self.msg = ' '   
        self.FONT = pygame.font.Font('Games\Assets\KeaniaOne-Regular.ttf',48)
        self.TEXT = ''
        self.TEXTSURFACE = self.FONT.render(self.TEXT,True,(0,255,255))
        self.x = x
        self.y = y
        self.inputRect = pygame.Rect(self.x,self.y,l,b)
        self.l = l
        self.active = False

    def print(self,eventype,surface):
        msg= "unknown"
        pos = pygame.mouse.get_pos()
        if self.inputRect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1: 
                self.active = True
                     
        if self.active:
            color = cyan
            msg =""
        else:
            color = transparentCyan

        if eventype == pygame.KEYDOWN:
            if self.active == True:
                if pygame.key == pygame.K_BACKSPACE:
                    msg = msg[:-1]
                    self.TEXT = self.TEXT[:-1]
                else:
                    msg+= pygame.unicode
                    self.TEXT+= pygame.event.unicode
                  
        pygame.draw.rect(surface,color,self.inputRect,2)
        surface.blit(self.TEXTSURFACE,(self.inputRect.x+5,self.inputRect.y+5))
        self.inputRect.w = max(self.l , self.TEXTSURFACE.get_width()+10)
        print( msg)



     

