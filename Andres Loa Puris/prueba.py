import random
import pygame
from pygame.locals import *

pygame.init()

class Pieza():
    
    # Constructor
    def __init__(self,index, largo, ancho):
        self.index = index
        self.Xo = 0
        self.Yo = 0
        self.color = (random.randint(10, 200),random.randint(10, 200),random.randint(10, 200))
        self.largo = largo
        self.ancho = ancho
        self.area = largo*ancho
        self.estado = 'N'
    
    # Metodos    
    def Informar(self):
        print(str(self.index)+" : "+str(self.Xo)+" , "+str(self.Yo)+" , "+str(self.estado))
        
    def Girar(self):
        aux = self.largo
        self.largo = self.ancho
        self.ancho = aux
        self.estado = 'N' if (self.estado == 'G') else 'G'

def OrdenarArreglo(piezas):
    areas = []
    for fig in piezas:
        areas.append(fig.area)
    orden = []
    areas = set(areas)
    areas = sorted(areas)
    areas.reverse()

    for i in range(len(areas)):
        for j in range(len(piezas)):
            if(areas[i] == piezas[j].area):
                for k in piezas:
                    if(k.index == piezas[j].index):
                        orden.append(k)
                j = len(piezas)
    return orden


def DataSet(data_name):
    with open(data_name) as f:
        w, h = [int(x) for x in next(f).split()] # read first line

        array = []
        for line in f: # read rest of lines
            array.append([x for x in line.split()])

    #Agregar
    formas = []
    for i in range(1,len(array)):
        for j in range(int(array[i][3])):
            formas.append(Pieza(array[i][0]+str(j+1),int(array[i][1]),int(array[i][2])))
    
    return w,h,formas    


largoTotal, anchoTotal, piezas = DataSet("DataExample.txt")

ventana = pygame.display.set_mode((largoTotal,anchoTotal))
soluciones = []

piezas = OrdenarArreglo(piezas)

#figuras.append(pygame.Rect(piezas[0].Xo,piezas[0].Yo,piezas[0].largo,piezas[0].ancho))
soluciones.append(pygame.Rect(piezas[0].Xo,piezas[0].Yo,piezas[0].largo,piezas[0].ancho))

def Algorithm(fig, figuras,largoTotal,anchoTotal):
    colision = True
    if(fig.ancho > fig.largo):
        fig.Girar()

    for i in range(largoTotal):
        for j in range(anchoTotal):
            fig.Xo = i
            fig.Yo = j
            for obj in figuras:
                if (pygame.Rect(fig.Xo,fig.Yo,fig.largo,fig.ancho).colliderect(obj) or (fig.Xo+fig.largo > largoTotal or fig.Yo+fig.ancho > anchoTotal) ):
                    colision = True
                    break
                else:
                    colision = False
                    
            if(colision == False):
                return fig


#if len(soluciones)!=len(piezas):
#        for fig in piezas:
#            soluciones.append(Algorithm(fig, figuras,largoTotal,anchoTotal))


while True:
    ventana.fill((255,255,255))

    while len(soluciones)!=len(piezas):
        for i in range(len(soluciones),len(piezas)):
            aux = Algorithm(piezas[i], soluciones,largoTotal,anchoTotal)
            soluciones.append(pygame.Rect(aux.Xo,aux.Yo,aux.largo,aux.ancho))

    for i in range(len(soluciones)):
        pygame.draw.rect(ventana,piezas[i].color,soluciones[i])
    


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update()