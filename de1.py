import sys,os
import pygame
finish = True
pygame.init()

os.system("cls")
print("Hello EXXON Engine Developer. May The Code With You!")
screen = pygame.display.init()
icon = pygame.image.load("icon.png")
pygame.display.set_caption("EXXON Engine Window")
pygame.display.set_icon(icon)
fps = pygame.time.Clock()
class Display:
    def set_fps(tick=60):
        fps.tick(tick)
    def set_witdh_height(width=600,height=600):
        global screen
        screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
        return screen 
    def set_color_screen(r=255,g=255,b=255):
        screen.fill((r,g,b))
    def start_screen(r=255,g=255,b=255): 
        Display.set_color_screen(r,g,b)
    def update_screen():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.update()
class Draws:
    def draw_rect(x,y,w,h,r,g,b):
        rect1 = pygame.draw.rect(screen,(r,g,b),pygame.Rect(x,y,w,h))
        return rect1
class Movements:
    def move_rects(object,x=0,y=0,w=0,h=0): 
        rect1 = pygame.draw.rect(screen,(125,234,124),pygame.Rect(object.x+x,object.y+y,w,h))
        return rect1
class Inputs:         
    class One_press:                            
        pass
    class Press:
        def d():
            keys1 = pygame.key.get_pressed()
            if keys1[pygame.K_d]:
                return 1
            else:
                
                return 0
        def a():
            keys1 = pygame.key.get_pressed()
            if keys1[pygame.K_a]:
                return 1
            else:
                return 0  
        def w():
            keys1 = pygame.key.get_pressed()
            if keys1[pygame.K_w]:
                return 1
            else:
                return 0  
        def s():
            keys1 = pygame.key.get_pressed()
            if keys1[pygame.K_s]:
                return 1
            else:
                return 0      
class Fonts():
    pass        
#class Updates:
    #class Draws_updates:
        #pass

    
