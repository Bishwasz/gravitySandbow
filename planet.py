import pygame
import math
class Planet:
    def __init__(self,xPosition,yPosition,veloY,veloX,surface, radius, mass, color):
        self.surface=surface
        self.radius=radius
        self.mass=mass
        self.color=color
        self.xPosition=xPosition
        self.yPosition=yPosition
        self.velXVector=[]
        self.velYVector=[]
        self.velocityX=0
        self.velocityY=0
        self.veloX=veloX
        self.veloY=veloY
    def draws(self):
        pygame.draw.circle(self.surface,self.color,(self.xPosition,self.yPosition),self.radius)
    def vector(self,item):
        for i in item:
            xOne=i.xPosition-i.xPosition
            yOne=i.yPosition-i.yPosition
            h=math.hypot(xOne,yOne)
            g=1
            force=(g*i.mass*i.mass)/(h**2)
            forceX=(xOne/h)*force
            forceY=(yOne/h)*force
            accX=forceX/i.mass
            accY=forceY/i.mass
            self.velX+=-accX
            self.velY+=-accY
            self.velXVector.append(self.velX)
            self.velYVector.append(self.velY)
    def update(self):
        self.veloY+=sum(self.velYVector)
        self.veloX+=sum(self.velXVector)
        self.xPosition+=self.veloX
        self.yPosition+=self.veloY
        self.velXVector=[]
        self.velYVector=[]