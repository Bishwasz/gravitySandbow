from tkinter import Button
import pygame
import math
from planet import Planet
import random
class Game:
    def __init__(self,gravitationalConstant, surface,displayWidth, displayHeight ):
        self.surface=surface
        self.displayWidth=displayWidth
        self.displayHeight= displayHeight
        self.gravitationalConstant=gravitationalConstant
        self.mainBool=True
        self.clock=pygame.time.Clock()
        self.items=[]
        self.button=Button((250,250,25),self.displayWidth-80,50,80,80,'+')
        self.buttonTwo=Button((250,250,25),0,50,80,80,'II')
        self.butOne=False
        self.butTwo=False
        self.pause=False
        self.size=20
        self.xa=0
        self.xb=0
        self.active=False

        self.drag=False
        self.mouse=pygame.mouse.get_pos()

        self.velX=0
        self.velY=0

        self.font=pygame.font.SysFont(None, 60)

        self.click=False

        self.menu=True
    def play(self):
        while self.mainBool:
            while self.menu:
                self.text()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit() 
                    if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_ESCAPE:
                           self.menu=False         
                           
            self.surface.fill((0,0,0))
            self.handle_events()
            pos=pygame.mouse.get_pos()
            if self.butOne and self.butTwo:
                pygame.draw.circle(self.surface,(200,200,200),(pos[0],pos[1]),self.size )
               
            if not self.butTwo:
                self.vector()
            self.draw()

            self.button.draw(self.surface,(0,0,0))
            self.buttonTwo.draw(self.surface,(0,0,0))
            pygame.display.update()
            self.clock.tick(40)
    def handle_events(self): 
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()

            if event.type==pygame.QUIT:
                self.mainBool=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.items=[]
                    self.butTwo=True
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if event.button==4 and self.butOne:
                    self.size-=4
                if event.button==5 and self.butOne:
                    self.size+=5
                if self.button.isOver(pos) :
                    self.butOne= not self.butOne
                if self.buttonTwo.isOver(pos) and not self.butOne:
                    self.butTwo= not self.butTwo
                if event.button == 1 and self.active:   
                    self.xa, self.xb=pygame.mouse.get_pos()
                    self.items.append(Planet(xPosition=pos[0],yPosition=pos[1],veloY=0,veloX=0,surface=self.surface,radius=self.size,mass=self.size**1.85,color=(random.randint(50,250),random.randint(50,250),random.randint(50,250))))
                    self.click=True
               
            if self.click:
                pygame.draw.line(self.surface,(250,250,250),(pos[0],pos[1]),(self.xa,self.xb))
            if event.type ==pygame.MOUSEBUTTONUP:
                
                if event.button==1 and self.active:
                    x=pygame.mouse.get_pos()[0]
                    y=pygame.mouse.get_pos()[1]
                    distance=math.hypot(pygame.mouse.get_pos()[0]-self.xa, pygame.mouse.get_pos()[1]-self.xb)
                    
                    self.velX=((self.xa-x))/(50)
                    self.velY=((self.xb-y))/(50)
                    # print('Distance:',distance,'  Velocity X:',self.velX, '   Velocity Y',self.velY)
                    # print(self.xa, x, self.xb,y)
                    # print(self.xa-x, self.xb-y)
                    self.items[len(self.items)-1].veloX=self.velX
                    self.items[len(self.items)-1].veloY=self.velY

                    self.butOne=False
                    self.active=False
                    self.click=False
                if self.butOne and self.buttonTwo:
                    self.active=True
                

                    
            if event.type ==pygame.MOUSEMOTION:
                if self.button.isOver(pos) or self.butOne:
                    self.button.color=(255,0,0) 
                else:
                    self.button.color=(0,255,0)

                if self.buttonTwo.isOver(pos)or self.butTwo:
                    self.buttonTwo.color=(255,0,0)
                else:
                    self.buttonTwo.color=(0,250,0)

    def vector(self):
        for i in self.items:
            velX=0
            velY=0
            for e in self.items:
                if not e==i:
                    xOne=i.xPosition-e.xPosition
                    yOne=i.yPosition-e.yPosition
                    h=math.hypot(xOne,yOne)
                    force=(self.gravitationalConstant*i.mass*e.mass)/(h**2)
                    forceX=(xOne/h)*force
                    forceY=(yOne/h)*force
                    accX=forceX/i.mass
                    accY=forceY/i.mass
                    velX+=-accX
                    velY+=-accY
                    i.velXVector.append(velX)
                    i.velYVector.append(velY)
                  
    def draw(self):
        for item in self.items:
            item.draws()
            if not self.butTwo:
                item.update()
    def messsage_to_screen(self,txt,color,x,y):
        message=self.font.render(txt, False, color)
        self.surface.blit(message,[x,y])
    def text(self):
        self.messsage_to_screen("Gravity SanDBox",(200,100,59),(self.displayWidth/2)-100,50)
        self.messsage_to_screen("To add bodies press Pause('II') and then after press +",(100,200,50),10,self.displayHeight//2)
        self.messsage_to_screen("Press Esc to start",(100,100,200),(self.displayWidth/2)-100,self.displayHeight*3/4)


class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
