import pygame
from pygame.locals import *
import random, math, sys
pygame.init()

#Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Tamanho da tela do jogo
Surface = pygame.display.set_mode((800,600))

Circulos = []
class Circulo:

    def __init__(self):

        self.radius = 30
        self.x = random.randint(self.radius, 800-self.radius)
        self.y = random.randint(self.radius, 600-self.radius)
        self.speedx = 0.5*(random.random()+1.0)
        self.speedy = 0.5*(random.random()+1.0)
        print(self.x)
for i in range(2):
    Circulos.append(Circulo())

def CircleCollide(C1,C2):
    C1Speed = math.sqrt((C1.speedx**2)+(C1.speedy**2))
    XDiff = -(C1.x-C2.x)
    YDiff = -(C1.y-C2.y)
    if XDiff > 0:
        if YDiff > 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff < 0:
        if YDiff > 0:
            Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff == 0:
        if YDiff > 0:
            Angle = -90
        else:
            Angle = 90
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    elif YDiff == 0:
        if XDiff < 0:
            Angle = 0
        else:
            Angle = 180
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    C1.speedx = XSpeed
    C1.speedy = YSpeed



def desenho():
    pygame.draw.circle(Surface, GREEN, (x, y), 10)

def CollisionDetect():
    pos = pygame.mouse.get_pos()
    raio = 30
    x = pos[0]
    y = pos[1]
    pygame.draw.circle(Surface, BLUE, (x, y), raio)
    for Circulo in Circulos:
        for Circulo2 in Circulos:
            if Circulo != Circulo2:
                if math.sqrt(  ((Circulo.x-Circulo2.x)**2)  +  ((Circulo.y-Circulo2.y)**2)  ) <= (Circulo.radius+Circulo2.radius):
                    CircleCollide(Circulo,Circulo2)


def movimento():
    raio = 30
    x,y = pygame.mouse.get_pos()

    for Circulo in Circulos:
        Circulo.x += Circulo.speedx
        Circulo.y += Circulo.speedy
        if Circulo.y > 580 or Circulo.y < 0:
            Circulo.speedy = Circulo.speedy * -1
        if Circulo.x > 780 or Circulo.x < 0:
            Circulo.speedx = Circulo.speedx * -1
        if math.sqrt( ((Circulo.x-x)**2) + ((Circulo.y - y)**2) ) <= (Circulo.radius+raio):
            print('Colidiu')


    #print ('CIRCULO X',int(Circulo.x))
    #print ('CIRCULO Y',int(Circulo.y))
    #print (' X  ',int(x))
    #print (' Y  ',int(y))


##def checar_colisao(player_rect,lista,placar):
##    colision_check = 0
##    colidiu = False
##    for colision_check in movimento():
##        colisao = movimento[colision_check].rect
##        if colisao.collidecircle(movimento()):
##            #print("Colisao X:",colisao.x," Y:",colisao.y)
##            placar = placar - 1
##            colidiu = True
##            colisao = colision_check
##    if colidiu == True:
##        lista = []
##    return [lista,placar]


def objetos():

    Surface.fill((0,0,0))
    raio = 30
    #x,y = pygame.mouse.get_pos()
    #print (x,y)
    pygame.draw.circle(Surface, BLUE, pygame.mouse.get_pos(), raio)
    for Circulo in Circulos:
        pygame.draw.circle(Surface, RED, (int(Circulo.x), int(600-Circulo.y)), Circulo.radius)
    pygame.display.flip()


def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit(); sys.exit()

def main():
    while True:
        GetInput()
        movimento()
        CollisionDetect()
        objetos()

if __name__ == '__main__': main()
