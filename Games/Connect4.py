import pygame
import button
import text
import os
import textBox

WIDTH,HEIGHT =  800, 800

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Connect 4")

BGCOLOUR = (21,28,28)
cyan = (0, 255 , 255)
transparentCyan = (10,142,142)
color = transparentCyan
WHITE = (255,255,255)

oggrid =   [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]

X = {0:155,1:205,2:255,3:305,4:355,5:405,6:455,7:505,8:555,9:605}
Y = {0:175,1:225,2:275,3:325,4:375,5:425,6:475,7:525,8:575,9:625}

FPS = 60

#---------------------------------------------------------Elements-------------------------------------------------
ROW0 = pygame.image.load(os.path.join('Games','Assets','0.png')).convert_alpha()
ROW1 = pygame.image.load(os.path.join('Games','Assets','1.png')).convert_alpha()
ROW2 = pygame.image.load(os.path.join('Games','Assets','2.png')).convert_alpha()
ROW3 = pygame.image.load(os.path.join('Games','Assets','3.png')).convert_alpha()
ROW4 = pygame.image.load(os.path.join('Games','Assets','4.png')).convert_alpha()
ROW5 = pygame.image.load(os.path.join('Games','Assets','5.png')).convert_alpha()
ROW6 = pygame.image.load(os.path.join('Games','Assets','6.png')).convert_alpha()
ROW7 = pygame.image.load(os.path.join('Games','Assets','7.png')).convert_alpha()
ROW8 = pygame.image.load(os.path.join('Games','Assets','8.png')).convert_alpha()
ROW9 = pygame.image.load(os.path.join('Games','Assets','9.png')).convert_alpha()
GRID = pygame.image.load(os.path.join('Games','Assets','Grid.png')).convert_alpha()
TITLE = pygame.image.load(os.path.join('Games','Assets','Connect4.png')).convert_alpha()
GAMEOVER = pygame.image.load(os.path.join('Games','Assets','GameOver.png')).convert_alpha()
RED_DOT_IMAGE = pygame.image.load(os.path.join('Games','Assets','Red.png')).convert_alpha()
RED_TINGE = pygame.image.load(os.path.join('Games','Assets','RedTinge.png')).convert_alpha()
EXIT_IMG = pygame.image.load(os.path.join('Games','Assets','ExitButton.png')).convert_alpha()
SAVE_IMG = pygame.image.load(os.path.join('Games','Assets','SaveButton.png')).convert_alpha()
QUIT_IMG = pygame.image.load(os.path.join('Games','Assets','QuitButton.png')).convert_alpha()
START_IMG = pygame.image.load(os.path.join('Games','Assets','StartButton.png')).convert_alpha()
YELLOW_DOT_IMAGE = pygame.image.load(os.path.join('Games','Assets','Yellow.png')).convert_alpha()
YELLOW_TINGE = pygame.image.load(os.path.join('Games','Assets','YellowTinge.png')).convert_alpha()
PLAYAGAIN_IMG = pygame.image.load(os.path.join('Games','Assets','PlayAgainButton.png')).convert_alpha()


#---------------------------------------------------------Buttons-----------------------------------------------------

QUIT = button.Button(450,478,QUIT_IMG,1)
EXIT = button.Button(271.5,487,EXIT_IMG,1)
SAVE = button.Button(271.5,583,SAVE_IMG,1)
START = button.Button(271.5,373,START_IMG,1)
PLAYAGAIN = button.Button(162,478,PLAYAGAIN_IMG,1)
ROW_0 = button.Button(150 , 116,ROW0,1)
ROW_1 = button.Button(200 , 116,ROW1,1)
ROW_2 = button.Button(250 , 116,ROW2,1)
ROW_3 = button.Button(300 , 116,ROW3,1)
ROW_4 = button.Button(350 , 116,ROW4,1)
ROW_5 = button.Button(400 , 116,ROW5,1)
ROW_6 = button.Button(450 , 116,ROW6,1)
ROW_7 = button.Button(500 , 116,ROW7,1)
ROW_8 = button.Button(550 , 116,ROW8,1)
ROW_9 = button.Button(600 , 116,ROW9,1)

#----------------------------------------------InputBoxes---------------------------------------------------
player_1 = textBox.TextBox(221.5,277,357,48)
player_2 = textBox.TextBox(221.5,459,357,48)
player_1_rect = pygame.Rect(221.5,277,357,48)
player_2_rect = pygame.Rect(221.5,459,357,48)

#------------------------------------------------TextBoxes---------------------------------------------------
Title = text.Text('WELCOME TO CONNECT 4',118,33,48)
Player1 = text.Text('Enter name of player 1',221.5,219,36)
Player2 = text.Text('Enter name of player 2',221.5,401,36)
Red_Turn = text.Text('Red\'s Turn',290,26,48)
Yellow_Turn = text.Text('Yellow\'s Turn',258,26,48)
Red_Wins = text.Text('Red Wins!!',286,21,48)
Yellow_Wins = text.Text('Yellow Wins!!',254,21,48)


rect = RED_DOT_IMAGE.get_rect()


#----------------------------------------------------Rectangles-------------------------------------------------
GRID_BOTTOM = pygame.Rect(142,657,515,10)
dot_rect = pygame.Rect(155,125,40,40)

def main():
    played = 0
    player = 1
    pos = 0
    clock = pygame.time.Clock()
    page = 0
    win = 0
    run =True
    while(run): 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
            

        WIN.fill(BGCOLOUR)

        if page == 1:
            if player == 1:
                #WIN.blit(RED_TINGE, (0, 0))
                Red_Turn.print(WIN)
            elif player == -1:
                #WIN.blit(YELLOW_TINGE, (0, 0))
                Yellow_Turn.print(WIN)
            WIN.blit(GRID, (148 , 168))
            if ROW_0.draw(WIN):
                row = 0  
                played = 1 
            elif ROW_1.draw(WIN):
                row = 1  
                played = 1 
            elif ROW_2.draw(WIN):
                row = 2   
                played = 1       
            elif ROW_3.draw(WIN):
                row = 3    
                played = 1        
            elif ROW_4.draw(WIN):
                row = 4   
                played = 1           
            elif ROW_5.draw(WIN):
                row = 5
                played = 1 
            elif ROW_6.draw(WIN):
                row = 6
                played = 1 
            elif ROW_7.draw(WIN):
                row = 7
                played = 1 
            elif ROW_8.draw(WIN):
                row = 8
                played = 1 
            elif ROW_9.draw(WIN):
                row = 9
                played = 1  
            
            if played == 1:
                pos = place(row,oggrid) 
                played = 0    
                if pos >= 0:    
                    oggrid[row][pos] = player
                    #print('*******')
                    page  = gamebreak(oggrid,player) 
                    player = player * -1
            display(oggrid)

        elif page == 0:
            win = 0
            oggrid =   [[0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]]
            player = 1
            played = 0
            WIN.blit(TITLE, (150.5, 125))
            if START.draw(WIN):
                page = 1
            if EXIT.draw(WIN):
                run = False

        elif page == 3:
            #WIN.blit(RED_TINGE, (0, 0))
            WIN.blit(GRID, (148 , 168))
            display(oggrid)
            Red_Wins.print(WIN)
            win = 1
            page = 5

        elif page == 4:
            #WIN.blit(YELLOW_TINGE, (0, 0))
            WIN.blit(GRID, (148 , 168))
            display(oggrid)
            Yellow_Wins.print(WIN)
            win = 1
            page = 6

        elif page == 5:
            #time.sleep(1)
            #WIN.blit(RED_TINGE, (0, 0))
            if win:
                for _ in range (0,1000000):
                    for ct in range (0,100):
                        pass
            win = 0 
            WIN.blit(GRID, (148 , 168))
            display(oggrid)
            Red_Wins.print(WIN)
            WIN.blit(GAMEOVER, (0,0))
            if QUIT.draw(WIN):
                run = False 
            if PLAYAGAIN.draw(WIN):
                page = 0 

        elif page == 6:
            #time.sleep(1)
            #WIN.blit(YELLOW_TINGE, (0, 0))
            if win:
                for _ in range (0,1000000):
                    for ct in range (0,100):
                        pass
            win = 0 
            WIN.blit(GRID, (148 , 168))
            display(oggrid)
            Yellow_Wins.print(WIN)
            WIN.blit(GAMEOVER, (0,0))
            if QUIT.draw(WIN):
                run = False 
            if PLAYAGAIN.draw(WIN):
                page = 0

        else:
            run = False
        
        pygame.display.update()
        
    pygame.quit()

def place(row,gamegrid):
    flag = 0
    for i in range (0,10):
        if (gamegrid[row][i] != 0):
            pos = i - 1
            flag = 1
            break
        if ( i == 9 and gamegrid[row][i] == 0 ):
            pos = 9
            flag = 1 
            break
    if flag == 0:
        pos =-1
    return pos

def display(gamegrid):
    for i in range (0,10):
        for j in range (0,10):
            if gamegrid[i][j] == 1:
                WIN.blit(RED_DOT_IMAGE,(X[i],Y[j]))
            elif gamegrid[i][j] == -1:
                WIN.blit(YELLOW_DOT_IMAGE,(X[i],Y[j]))

def gamebreak(gamegrid,pno):
    value = 1
    for i in range (0,10):
        #print('######')
        for j in range (0,10):
            #print (i)
            #print (j)
            if(gamegrid[i][j] == pno):
                #print('???????')
                value  = check(gamegrid,pno,i,j)
                if value == 3 or value == 4:
                    return value
            #print('-----')
    return value

def check(gamegrid,pno,i,j):
    
    if(i+3<10):
        x=1
        y=0
        if check4(gamegrid,i,j,x,y,pno):
            if pno == 1:
                return 3
            elif pno == -1:
                return 4 
        
    if(j+3<10):
        x=0
        y=1
        if check4(gamegrid,i,j,x,y,pno):
            if pno == 1:
                return 3
            elif pno == -1:
                return 4 
    if(i-3>=0):
        x=-1
        y=0
        if check4(gamegrid,i,j,x,y,pno):
            if pno == 1:
                return 3
            elif pno == -1:
                return 4 
    if(j-3>=0):
        x=0
        y=-1
        if check4(gamegrid,i,j,x,y,pno):
            if pno == 1:
                return 3
            elif pno == -1:
                return 4 
    if(j+3<10 and i+3<10):
        x=1
        y=1
        if check4(gamegrid,i,j,x,y,pno):
            if pno == 1:
                return 3
            elif pno == -1:
                return 4 
    if(j+3<10 and i-3>=0):
        x=-1
        y=1
        if check4(gamegrid,i,j,x,y,pno):
            #print('^^^^^^^')
            #print(check4(gamegrid,i,j,x,y,pno))
            if pno == 1:
                return 3
            elif pno == -1:
                return 4        
    if(j-3>=0 and i+3<10):
        x=1
        y=-1
        if check4(gamegrid,i,j,x,y,pno):
            if pno == 1:
                return 3
            elif pno == -1:
                return 4 
    if(j-3>=0 and i-3>=0):
        x=-1
        y=-1  
        if check4(gamegrid,i,j,x,y,pno):
            if pno == 1:
                return 3
            elif pno == -1:
                return 4
    return 1
            
def check4(gamegrid,r,c,x,y,pno):
    ct = 0 
    for k in range (1,4):
        if(gamegrid[r+(k*x)][c+(k*y)] == pno):
            ct+=1
    if ct == 3:
        return 1
    else:
        return 0 
    
if __name__ == "__main__":
    main() 