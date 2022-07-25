from planet import Planet
from game import Game
import pygame
def main():
    width=1200 # Width of Card
    height=900 # height of Cards
    pygame.init()
    pygame.display.set_mode((width,height)) # Display description
    surface=pygame.display.get_surface()
    mainGame=Game(gravitationalConstant=1.3,surface=surface, displayWidth=width,displayHeight=height)
    mainGame.play()
    pygame.quit()
main()