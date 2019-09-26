
# coding: utf-8

# In[25]:
import math

class Pieza():
    largo = 0
    ancho = 0
    index = ""
    # Constructor
    def __init__(self,index, ancho, largo):
        self.index = index
        self.coordX = 0
        self.coordY = 0
        self.largo = largo
        self.ancho = ancho
        self.area = largo*ancho
        self.estado = 'N'
    
    # Metodos    
    def Informar(self):
        print(str(self.index)+" : "+str(self.coordX)+" , "+str(self.coordY)+" , "+str(self.estado))
    
    def __cmp__(self,other):
        if self.area < other.area:
            rst = -1
        elif self.area > other.area:
            rst = 1
        else:
            rst=0
        return rst
        
    def Girar(self):
        aux = self.largo
        self.largo = self.ancho
        self.ancho = aux
        self.estado = 'N' if (self.estado == 'G') else 'G'




"""class MaxRectBinPack():
     # Constructor
      def __init__(self,ancho, largo):
          self.ancho = ancho
          self.largo = largo
          self.usedRect = []
          self.freeRect = []
          
      def FindPositionForBestFit( ancho, alto,mejorArea,mejorAjusteLateral):
         rect = Pieza()
         mejorArea = 9999999
         mejorAjusteLateral = 9999999
         n = len(freeRect)
         for i in range (n):
             areaFit = freeRect[i].ancho * freeRect[i].alto

             if(freeRect[i].ancho >= ancho and freeRect[i].largo >= largo):
                 leftoverHoriz = abs(freeRect[i].ancho - ancho)
                 leftoverVert = abs(freeRect[i].largo - largo)
                 AjusteLateral = min(leftoverHoriz,leftoverVert)
                 if(areaFit < mejorArea or (areaFit == mejorArea and AjusteLateral<mejorAjusteLateral)):
                     rect.coordX = freeRect[i].coordX
                     rect.coordY = freeRect[i].coordY
                     rect.ancho = freeRect[i].ancho
                     rect.largo = freeRect[i].largo
                     mejorAjusteLateral = AjusteLateral
                     mejorArea = areaFit

             if (freeRect[i].ancho>=largo and freeRect[i].largo >= ancho):
                leftoverHoriz = abs(freeRect[i].ancho - alto)
                leftoverVert = abs(freeRect[i].alto - ancho)
                AjusteLateral = min (leftoverHoriz,leftoverVert)
                if(areaFit < mejorArea or (areaFit == mejorArea and AjusteLateral < mejorAjusteLateral )):
                    rect.coordX = freeRect[i].coordX
                    rect.coordY = freeRect[i].coordY
                    rect.ancho = alto
                    rect.alto = ancho
                    mejorAjusteLateral = AjusteLateral
                    mejorArea = areaFit
         return rect
"""


# In[26]:


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


# In[27]:


"""
largoTotal = int(input(" Ingrese largo de la plancha :"))
anchoTotal = int(input(" Ingrese ancho de la plancha :"))

N = int(input("Cantidad de Piezas :"))
n , piezas = 1 , []


# Imput valores
while n <= N:
    index = input(" Ingrese index :")
    largo = int(input(" Ingrese largo :"))
    ancho = int(input(" Ingrese ancho :"))
    cantidad = int(input(" Ingrese cantidad :"))
    print("  ")
    
    for i in range(cantidad):
        piezas.append(Pieza(index+str(i+1),largo,ancho))
    n+= cantidad
 """   


#DataSet (.txt)
largoTotal, anchoTotal, piezas = DataSet("DataExample.txt")    
# -> TODO: Colocar Algoritmo de Empaquetamiento ...
piezasord = sorted(piezas, key = lambda objeto: objeto.area)
usedRectangles = []
freeRectangles = []
freeRectangles.append(Pieza(" ",anchoTotal,largoTotal))

def SaltarEspacioLibre(piezaLibre,espacioUsado):
    if(espacioUsado.coordX >= piezaLibre.coordX + piezaLibre.ancho or espacioUsado.coordX + espacioUsado.ancho <= piezaLibre.coordX or espacioUsado.coordY >= piezaLibre.coordY + piezaLibre.largo or espacioUsado.coordY + espacioUsado.largo <= piezaLibre.coordY):
     return False
    
    if(espacioUsado.coordX < piezaLibre.coordX + piezaLibre.ancho and espacioUsado.coordX + espacioUsado.ancho > piezaLibre.coordX):
        ## Nuevo rect arriba del rectangulo usado
        if(espacioUsado.coordY > piezaLibre.coordY and espacioUsado.coordY < piezaLibre.coordY + piezaLibre.largo):
            newRect = piezaLibre
            newRect.largo = espacioUsado.coordY - espacioUsado.coordY
            freeRectangles.append(newRect)
        ## Nuevo rect abajo del rectangulo usado
        if(espacioUsado.coordY + espacioUsado.largo < piezaLibre.coordY+ piezaLibre.largo):
            newRect = piezaLibre
            newRect.coordY = espacioUsado.coordY + espacioUsado.largo
            newRect.largo = piezaLibre.coordY + piezaLibre.largo - (espacioUsado.coordY+ espacioUsado.largo)
            freeRectangles.append(newRect)
    
    if(espacioUsado.coordY < piezaLibre.coordY + piezaLibre.largo and espacioUsado.coordY + espacioUsado.largo > piezaLibre.coordY):
        ## Nuevo rect a la izquierda del rectangulo usado
        if(espacioUsado.coordX > piezaLibre.coordX and espacioUsado.coordX < piezaLibre.coordX + piezaLibre.ancho):
         newRect = piezaLibre
         newRect.ancho = espacioUsado.coordX - newRect.coordX
         freeRectangles.append(newRect)
        if(espacioUsado.coordX + espacioUsado.ancho < piezaLibre.coordX + piezaLibre.ancho):
            newRect = piezaLibre
            newRect.coordX = espacioUsado.coordX + espacioUsado.ancho
            newRect.ancho = piezaLibre.coordX + piezaLibre.ancho - (espacioUsado.coordX + espacioUsado.ancho)
            freeRectangles.append(newRect)
    return True

def FindPositionForBestFit(ancho,largo,mejorArea,mejorAjusteLateral):
         rect = Pieza("",0,0)
         mejorArea = 9999999
         mejorAjusteLateral = 9999999
         n = len(freeRectangles)
         for i in range (n):
             areaFit = freeRectangles[i].ancho * freeRectangles[i].largo

             if(freeRectangles[i].ancho >= ancho and freeRectangles[i].largo >= largo):
                 leftoverHoriz = abs(freeRectangles[i].ancho - ancho)
                 leftoverVert = abs(freeRectangles[i].largo - largo)
                 AjusteLateral = min(leftoverHoriz,leftoverVert)
                 if(areaFit < mejorArea or (areaFit == mejorArea and AjusteLateral<mejorAjusteLateral)):
                     rect.coordX = freeRectangles[i].coordX
                     rect.coordY = freeRectangles[i].coordY
                     rect.ancho = freeRectangles[i].ancho
                     rect.largo = freeRectangles[i].largo
                     mejorAjusteLateral = AjusteLateral
                     mejorArea = areaFit

             if (freeRectangles[i].ancho>=largo and freeRectangles[i].largo >= ancho):
                leftoverHoriz = abs(freeRectangles[i].ancho - largo)
                leftoverVert = abs(freeRectangles[i].largo - ancho)
                AjusteLateral = min (leftoverHoriz,leftoverVert)
                if(areaFit < mejorArea or (areaFit == mejorArea and AjusteLateral < mejorAjusteLateral )):
                    rect.coordX = freeRectangles[i].coordX
                    rect.coordY = freeRectangles[i].coordY
                    rect.ancho = largo
                    rect.largo = ancho
                    mejorAjusteLateral = AjusteLateral
                    mejorArea = areaFit
         return rect

def LimpiarRectangulosdelaLista():
    n = len(freeRectangles)
    for m in range (0,m<n-1,m=m+1):
        if(freeRectangles[m].coordX == freeRectangles[m+1].coordX and freeRectangles[m].coordY == freeRectangles[m+1].coordY and freeRectangles[m].ancho == freeRectangles[m].largo and freeRectangles[m].largo == freeRectangles[m+1].largo):
            freeRectangles.remove(freeRectangles[m])
            m=m-1

def ScoreRect(ancho,largo,score1,score2):
    newRect = Pieza(" ",ancho,largo)
    score1 = 999999
    score2 = 999999
    newRect = FindPositionForBestFit(ancho,largo,score1,score2)
    if(newRect.largo == 0):
        return
    return newRect

def UbicarRect(pieza):
    n = len(freeRectangles)    
    for i in range(0,n):
        if(SaltarEspacioLibre(freeRectangles[i],pieza)):
            freeRectangles.remove(freeRectangles[i])
            i = i-1
            n = n-1    
    
    LimpiarRectangulosdelaLista()
    usedRectangles.append(pieza)

def InsertarRects(ancho,largo):
    score1 = 999999
    score2 = 999999
    newRect = FindPositionForBestFit(ancho,largo,score1,score2)
    if(newRect == largo):
        return newRect

   
    

    
    n = len(freeRectangles)    
    for i in range(0,n):
        if(SaltarEspacioLibre(freeRectangles[i],newRect)):
            freeRectangles.remove(freeRectangles[i])
            i = i-1
            n = n-1    
    
    ##LimpiarRectangulosdelaLista()
    usedRectangles.append(newRect)
    return newRect
    
cantP = len(piezasord)

for l in range(cantP):
       InsertarRects(piezasord[l].ancho,piezasord[l].largo) 

    
    

# Informar Piezas
for fig in usedRectangles:
        fig.Informar()

# Mostrar Piezas       
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

codes = [
    Path . MOVETO ,
    Path . LINETO ,
    Path . LINETO ,
    Path . LINETO ,
    Path . CLOSEPOLY ,
]

fig , ax = plt . subplots ()

for fig in usedRectangles:
    verts = [
        ( fig.coordX , fig.coordY ),  # Xo , Yo
        ( fig.coordX , fig.coordY+ fig.ancho ),  # Xo , Yo + ancho
        ( fig.coordX + fig.largo , fig.coordY + fig.ancho),  # Xo + largo , Yo + ancho
        ( fig.coordX + fig.largo , fig.coordY ),  # Xo +largo , Yo
        ( 0. , 0. ),  # Ignorar
    ]

    path = Path ( verts , codes )
    patch = patches . PathPatch ( path , facecolor = 'cyan' , lw = 1 )
    ax . add_patch ( patch )
    
ax . set_xlim ( 0 , largoTotal)
ax . set_ylim ( 0 , anchoTotal)
plt . show ()



#%%


#%%


#%%
