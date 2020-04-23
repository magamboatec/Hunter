import pygame
import random
import sys
pygame.init()
gameDisplay = pygame.display.set_mode((740,740),0,32)
pygame.display.set_caption("Hunter")
programIcon = pygame.image.load('media//computer.png')
pygame.display.set_icon(programIcon)

pygame.mixer.init()
music=pygame.mixer.music.load("media//moonTheme.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
playerImg = pygame.transform.scale(pygame.image.load("media//player.png"),(75,75))
computerImg = pygame.transform.scale(pygame.image.load("media//computer.png"),(75,75))
fieldImg =  pygame.image.load("media//field.png")
visitedImg = pygame.transform.scale(pygame.image.load("media//fire.png"),(10,10))
unvisitedImg = pygame.transform.scale(pygame.image.load("media//green.png"),(10,10))
startButtonImg = pygame.transform.scale(pygame.image.load("media//startButton.png"),(176,112))
lvl1Img = pygame.transform.scale(pygame.image.load("media//lvl1.png"),(176,75))
lvl2Img = pygame.transform.scale(pygame.image.load("media//lvl2.png"),(176,75))
hpImg = pygame.transform.scale(pygame.image.load("media//lifes.png"),(50,50))
gameOverImg = pygame.image.load("media//gameover.png")
winnerImg = pygame.image.load("media//win.png")
cupImg = pygame.transform.scale(pygame.image.load("media//cup.png"),(600,600))

level=1
hp = 3 

already = []
gameMatrix =  [[(75,75),(150,75),(225,75),(300,75),(375,75),(450,75),(525,75),(600,75)],
              [(75,150),(150,150),(225,150),(300,150),(375,150),(450,150),(525,150),(600,150)],
              [(75,225),(150,225),(225,225),(300,225),(375,225),(450,225),(525,225),(600,225)],
              [(75,300),(150,300),(225,300),(300,300),(375,300),(450,300),(525,300),(600,300)],
              [(75,375),(150,375),(225,375),(300,375),(375,375),(450,375),(525,375),(600,375)],
              [(75,450),(150,450),(225,450),(300,450),(375,450),(450,450),(525,450),(600,450)],
              [(75,525),(150,525),(225,525),(300,525),(375,525),(450,525),(525,525),(600,525)],
              [(75,600),(150,600),(225,600),(300,600),(375,600),(450,600),(525,600),(600,600)]]

i = 75
lista=[]
while i<=601:
    lista.append(i)
    i+=5

i = 75
lista2=[]
while i<601:
    lista2.append(i)
    i+=75
    
playerSurf = ""
computerSurf =""
computerSurf2 = ""




def isEnd():
    for row in lista2:
        for col in lista:
            if not((row,col) in already):
                return False
    for row in lista2:
        for col in lista:
            if not((col,row) in already):
                return False
    return True        
                
def drawPath():
    for row in lista2:
        for col in lista:
            gameDisplay.blit(unvisitedImg, (col+35,row+50))
    for row in lista2:
        for col in lista:
            gameDisplay.blit(unvisitedImg, (row+35,col+50)) 
    for i in already:
        gameDisplay.blit(visitedImg, (i[0]+35,i[1]+50))      

def isValidMove(pos,orient,up):
    global already
    radio=20
    if(orient==1): #horizontal
        for col in lista2:
            if (pos[0]<=col+radio and pos[0]>=col-radio): 
                if(pos[0]<=600 and pos[0]>=75) and (pos[1]<=600 and pos[1]>=75):
                    if(pos[0]<col):
                        step=col-abs(col-pos[0])
                        while step<=col:
                            if up:
                                already.append((step,pos[1]+5))
                            else:
                                already.append((step,pos[1]-5))
                            step+=5
                    elif(pos[0]>col):
                        step=col+abs(col-pos[0])
                        while step>=col:
                            if up:
                                already.append((step,pos[1]+5))
                            else:
                                already.append((step,pos[1]-5))
                            step-=5
                    return (col,pos[1])

    elif(orient==0):# vertical
        for col in lista2:        
            if (pos[1]<=col+radio and pos[1]>=col-radio):    
                if(pos[0]<=600 and pos[0]>=75) and (pos[1]<=600 and pos[1]>=75):        
                    if(pos[1]<col):
                        step=col-abs(col-pos[1])
                        while step<=col:
                            if up:
                                already.append((pos[0]-5,step))
                            else:
                                already.append((pos[0]+5,step))
                            step+=5
                    elif(pos[1]>col):
                        step=col+abs(col-pos[1])
                        while step>=col:
                            if up:
                                already.append((pos[0]-5,step))
                            else:
                                already.append((pos[0]+5,step))
                            step-=5
                    return (pos[0],col)
    else:# computer
        for col in lista2:        
            if (pos[0]==col or pos[1]==col):    
                if(pos[0]<=600 and pos[0]>=75) and (pos[1]<=600 and pos[1]>=75):
                    return (pos)        
        
    return (-1,-1)

    
def drawplayer(x,y):
    global playerSurf,computerSurf,already
    already.append((x,y))
    drawPath()
    playerSurf= gameDisplay.blit(playerImg, (x,y))
def execute():
    global computerSurf,playerSurf,computerSurf2,hp
    gameDisplay.blit(fieldImg, (50,50))
    music=pygame.mixer.music.load("media//moonTheme.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    done = False
    drawPath()
    
    randomRowP = random.choice(lista2)
    randomColP = random.choice(lista2)
    playerSurf = gameDisplay.blit(playerImg, (randomRowP,randomColP))

    while True:
        randomRowC = random.choice(lista2)
        randomColC = random.choice(lista2)
        if(abs(randomRowP-randomRowC)>225 and abs(randomColP-randomColC)>225):
            break
    computerSurf = gameDisplay.blit(computerImg,(randomRowC,randomColC))    
    if level==2:    
        while True:
            randomRowC2 = random.choice(lista2)
            randomColC2 = random.choice(lista2)
            if(abs(randomRowP-randomRowC2)>75 and abs(randomColP-randomColC2)>75) and (abs(randomRowC-randomRowC2)>=150 and abs(randomColC-randomColC2)>=150):
                break
        computerSurf2 = gameDisplay.blit(computerImg,(randomRowC2,randomColC2))
        gameDisplay.blit(lvl2Img, (310,55))
    elif level==1:
        gameDisplay.blit(lvl1Img, (310,55))
    
    if hp>0:
        for i in range(hp):
            gameDisplay.blit(hpImg, (540+(i*50),61))
    else:
        gameOver()
    
    startSurf = gameDisplay.blit(startButtonImg, (40,38))
    while not done:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
                exit()                
            if event.type == pygame.KEYDOWN:
                if(event.key==13):
                    if level==1:
                        startLvl1()
                    else:
                        startLvl2()
                       
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startSurf.collidepoint(pygame.mouse.get_pos()):
                    if(level==1):
                        startLvl1()
                    else:
                        startLvl2()
                 
        pygame.display.update()
        clock.tick(20)        
    pygame.quit()

def gameOver(): 
    gameDisplay.blit(fieldImg, (50,50))
    gameDisplay.blit(gameOverImg, (100,350))
    done =False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
                exit()                
            if event.type == pygame.KEYDOWN:
                if(event.key==13):
                    done = True
                    pygame.quit()
                    sys.exit()
                    exit()

        pygame.display.update()
        clock.tick(20)        
    pygame.quit()
def winDisplay():   
    gameDisplay.blit(fieldImg, (50,50))
    gameDisplay.blit(cupImg, (70,70))
    gameDisplay.blit(winnerImg, (150,275))
    done =False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
                exit()                
            if event.type == pygame.KEYDOWN:
                if(event.key==13):
                    done = True
                    pygame.quit()
                    sys.exit()
                    exit()

        pygame.display.update()
        clock.tick(20)        
    pygame.quit()    
def startLvl1():
    global already,level,hp
    music=pygame.mixer.music.load("media//menu.mp3")
    pygame.mixer.music.set_volume(2)
    pygame.mixer.music.play(-1)
    done = False
    xplayer = 0
    yplayer = 0
    xcomp = computerSurf.x
    ycomp = computerSurf.y
    compSpeed = 5
    rateWin = 5
    orient=1
    up= False
    while not done:
        for event in pygame.event.get():     
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                exit()
            if event.type == pygame.KEYDOWN:
                if(event.key==pygame.K_RIGHT):
                    xplayer=5
                    orient=0
                    up=True
                elif(event.key==pygame.K_LEFT):
                    xplayer=-5
                    orient=0
                    up=False
                elif(event.key==pygame.K_UP):
                    yplayer=-5
                    orient=1
                    up=True
                elif(event.key==pygame.K_DOWN):
                    yplayer=5
                    orient=1
                    up=False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xplayer=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN :
                    yplayer=0
        gameDisplay.blit(fieldImg, (50,50))              
        pos=(isValidMove((playerSurf.x+xplayer,playerSurf.y+yplayer),orient,up))
        if pos!=(-1,-1):
            drawplayer(pos[0],pos[1])
        else:
            drawplayer(playerSurf.x,playerSurf.y)
        if isEnd():
            level+=1
            done = True
            
        if(xcomp>=playerSurf.x+xplayer-rateWin and xcomp<=playerSurf.x+xplayer+rateWin) and (ycomp>=playerSurf.y+yplayer-rateWin and ycomp<=playerSurf.y+yplayer+rateWin):
            hp-=1
            done = True
        else:
            if(xcomp>=playerSurf.x):
                pos=isValidMove((xcomp-compSpeed,ycomp),3,False)
                if pos!=(-1,-1):
                    xcomp-=compSpeed
            else:               
                pos=(isValidMove((xcomp+compSpeed,ycomp),3,False))
                if pos!=(-1,-1):
                    xcomp+=compSpeed                   
            if(ycomp>=playerSurf.y):                
                pos=(isValidMove((xcomp,ycomp-compSpeed),3,False))
                if pos!=(-1,-1):        
                    ycomp-=compSpeed
            else:            
                pos=(isValidMove((xcomp,ycomp+compSpeed),3,False))
                if pos!=(-1,-1):
                    ycomp+=compSpeed                         
        
        gameDisplay.blit(computerImg,(xcomp,ycomp))
        gameDisplay.blit(lvl1Img, (310,55))
        for i in range(hp):
            gameDisplay.blit(hpImg, (540+(i*50),61))  
        pygame.display.update()
        clock.tick(25)
        
    already = []
    
    execute()
    
def startLvl2():
    global already,level,hp
    music=pygame.mixer.music.load("media//menu.mp3")
    pygame.mixer.music.set_volume(2)
    pygame.mixer.music.play(-1)
    done = False
    xplayer = 0
    yplayer = 0
    xcomp = computerSurf.x
    ycomp = computerSurf.y
    xcomp2 = computerSurf2.x
    ycomp2 = computerSurf2.y    
    compSpeed = 5
    rateWin = 5
    orient=1
    up=False
    while not done:
        for event in pygame.event.get():     
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                exit()
            if event.type == pygame.KEYDOWN:
                if(event.key==pygame.K_RIGHT):
                    xplayer=5
                    orient=0
                    up=True
                elif(event.key==pygame.K_LEFT):
                    xplayer=-5
                    orient=0
                    up=False
                elif(event.key==pygame.K_UP):
                    yplayer=-5
                    orient=1
                    up=True
                elif(event.key==pygame.K_DOWN):
                    yplayer=5
                    orient=1
                    up=False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xplayer=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN :
                    yplayer=0
        gameDisplay.blit(fieldImg, (50,50))              
        pos=(isValidMove((playerSurf.x+xplayer,playerSurf.y+yplayer),orient,up))
        if pos!=(-1,-1):
            drawplayer(pos[0],pos[1])
        else:
            drawplayer(playerSurf.x,playerSurf.y)
        if isEnd():          
            winDisplay()
            
        if(xcomp>=playerSurf.x+xplayer-rateWin and xcomp<=playerSurf.x+xplayer+rateWin) and (ycomp>=playerSurf.y+yplayer-rateWin and ycomp<=playerSurf.y+yplayer+rateWin):
            hp-=1
            done = True
        else:
            if(xcomp>=playerSurf.x):
                pos=isValidMove((xcomp-compSpeed,ycomp),3,False)
                if pos!=(-1,-1):
                    xcomp-=compSpeed
            else:               
                pos=(isValidMove((xcomp+compSpeed,ycomp),3,False))
                if pos!=(-1,-1):
                    xcomp+=compSpeed                   
            if(ycomp>=playerSurf.y):                
                pos=(isValidMove((xcomp,ycomp-compSpeed),3,False))
                if pos!=(-1,-1):        
                    ycomp-=compSpeed
            else:            
                pos=(isValidMove((xcomp,ycomp+compSpeed),3,False))
                if pos!=(-1,-1):
                    ycomp+=compSpeed                  
        if(xcomp2>=playerSurf.x+xplayer-rateWin and xcomp2<=playerSurf.x+xplayer+rateWin) and (ycomp2>=playerSurf.y+yplayer-rateWin and ycomp2<=playerSurf.y+yplayer+rateWin):
            hp-=1
            done = True
        else:
            if(xcomp2>=playerSurf.x):
                pos=isValidMove((xcomp2-compSpeed,ycomp2),3,False)
                if pos!=(-1,-1):
                    xcomp2-=compSpeed
            else:               
                pos=(isValidMove((xcomp2+compSpeed,ycomp2),3,False))
                if pos!=(-1,-1):
                    xcomp2+=compSpeed                   
            if(ycomp2>=playerSurf.y):                
                pos=(isValidMove((xcomp2,ycomp2-compSpeed),3,False))
                if pos!=(-1,-1):        
                    ycomp2-=compSpeed
            else:            
                pos=(isValidMove((xcomp2,ycomp2+compSpeed),3,False))
                if pos!=(-1,-1):
                    ycomp2+=compSpeed                      
        gameDisplay.blit(computerImg,(xcomp,ycomp))           
        gameDisplay.blit(computerImg,(xcomp2,ycomp2))
        gameDisplay.blit(lvl2Img, (310,55))
        for i in range(hp):
            gameDisplay.blit(hpImg, (540+(i*50),61))        
        pygame.display.update()
        clock.tick(46)
        
    already = []
    execute()     
execute()  
