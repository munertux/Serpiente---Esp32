import random
from machine import Pin as pin
from utime import sleep,sleep_ms
guia=[
    [0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,2 ,17,5 ,22,0 ],
    [15,4 ,16,19,1,23],
    [15,12,14,25,33,23],
    [0 ,13,27,26,32,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ],
    ]
matriz=[2,17,5,22,4,16,19,21,12,14,25,33,13,27,26,32,23,15]
instanciador=[[0 ,0 ,0 ,0 ,0 ,0 ],
              [0],
              [pin(15,pin.OUT)],
              [pin(15,pin.OUT)],
              [0],
              [0 ,0 ,0 ,0 ,0 ,0 ],
              ]
botonW=pin(36,pin. IN)
subir=pin(39,pin. IN)
bajar=pin(23,pin. IN)
botonD=pin(18,pin. IN)
botonS=pin(34,pin. IN)
botonA=pin(35,pin. IN)
inicio=0
final=4
for x in range(1,5):
   
    for i in matriz[inicio:final]:
        instanciador[x].append (pin(i,pin. OUT))
    if(x==1 or x==4):
        instanciador[x].append(0)
    else:
        instanciador[x].append((pin(15,pin. OUT)))
    final=final+4
    inicio=inicio+4

def animacion():
    for fila in range(1,5):
        for columna in range(1,5):
            instanciador[fila][columna].value(1)
            sleep(0.06)            
    for fila in reversed(range(1,5)):
        for columna in reversed(range(1,5)):
            instanciador[fila][columna].value(0)
            sleep(0.06)    
   
def serpiente():
    instanciador[1][1].value(1)
    puntaje=0
    manzana=0
    manzanaSpawn=0
    columna=1
    fila=1
    a=0
    velocidad=5
    anaconda=[instanciador[1][1]]
    while True:
        if(subir.value()==0):
            velocidad=velocidad-5    
        if(bajar.value()==0):
            velocidad=velocidad+5          
        if (botonD.value()==0):
            if(manzanaSpawn==0):
                while True:
                    manzana=instanciador[random.randint(1,4)][random.randint(1,4)]
                    if(manzana not in anaconda):
                        manzana.value(1)
                        manzanaSpawn=1
                        break
            while (columna<6 and botonW.value()==1 and botonS.value()==1):
                    columna=columna+1
                    if(instanciador[fila][columna]==manzana):
                        puntaje=1
                       
                        manzanaSpawn=0
                       
                       
                    if(columna>=1 and columna<5  ):
                        instanciador[fila][columna].value(1)
                       
                           
                        anaconda.insert(0,instanciador[fila][columna])

                    if(columna>1 ):
                        if(puntaje==0):
                            anaconda[len(anaconda)-1].value(0)
                            anaconda.pop(len(anaconda)-1)

                           
                       

                        if(columna==5 or instanciador[fila][columna] in anaconda[1:len(anaconda)]):
                           
                            for x in range(0,3):
                                instanciador[fila][columna-1].value(1)
                                instanciador[2][0].value(1)
                                instanciador[2][5].value(1)
                                sleep(0.2)
                                instanciador[2][0].value(0)
                                instanciador[2][5].value(0)
                                instanciador[fila][columna-1].value(0)
                                sleep(0.2)
                            manzana.value(0)
                            animacion()
                            serpiente()
                       
                        while(botonW.value()==1 and botonS.value()==1 and a<=velocidad):
                            if(subir.value()==0):
                                velocidad=velocidad-2
                            if(bajar.value()==0):  
                                velocidad=velocidad+2                                                            
                            if(puntaje==1):
                                sleep(0.05)
                            else:
                                sleep(0.2)
                            a=a+1
                        a=0
                        puntaje=0
        if (botonS.value()==0):
            if(manzanaSpawn==0):
                while True:
                    manzana=instanciador[random.randint(1,4)][random.randint(1,4)]
                    if(manzana not in anaconda):
                        manzana.value(1)
                        manzanaSpawn=1
                        break            
            while (fila<6 and botonD.value()==1 and botonA.value()==1):
                    fila=fila+1
                    if(instanciador[fila][columna]==manzana):
                        puntaje=1
                        manzanaSpawn=0
                       
                    if(fila>=1 and fila<5  ):
                        instanciador[fila][columna].value(1)
                        anaconda.insert(0,instanciador[fila][columna])
                    if(fila>1 ):
                        if(puntaje==0):
                            anaconda[len(anaconda)-1].value(0)
                            anaconda.pop(len(anaconda)-1)                          
               
                        if(fila==5  or instanciador[fila][columna] in anaconda[1:len(anaconda)]):
                            for x in range(0,3):
                                instanciador[fila-1][columna].value(1)
                                instanciador[2][0].value(1)
                                instanciador[2][5].value(1)
                                sleep(0.2)
                                instanciador[2][0].value(0)
                                instanciador[2][5].value(0)
                                instanciador[fila-1][columna].value(0)
                                sleep(0.2)
                            manzana.value(0)
                            animacion()
                            serpiente()
                        while(botonD.value()==1 and botonA.value()==1 and a<=velocidad):
                            if(subir.value()==0):
                                velocidad=velocidad-2
                            if(bajar.value()==0):  
                                velocidad=velocidad+2                                
                            if(puntaje==1):
                                sleep(0.05)
                            else:
                                sleep(0.2)
                            a=a+1
                        a=0
                        puntaje=0
        if (botonA.value()==0):
            if(manzanaSpawn==0):
                while True:
                    manzana=instanciador[random.randint(1,4)][random.randint(1,4)]
                    if(manzana not in anaconda):
                        manzana.value(1)
                        manzanaSpawn=1
                        break            
            while (columna<6 and botonW.value()==1 and botonS.value()==1):
                    columna=columna-1
                    if(instanciador[fila][columna]==manzana):
                        puntaje=1
                        manzanaSpawn=0
                    if(columna>=1 and columna<5  ):
                        instanciador[fila][columna].value(1)
                        anaconda.insert(0,instanciador[fila][columna])
                    if(columna<5):
                        if(puntaje==0):
                            anaconda[len(anaconda)-1].value(0)
                            anaconda.pop(len(anaconda)-1)
                       
                         
                        if(columna==0  or instanciador[fila][columna] in anaconda[1:len(anaconda)]):
                            for x in range(0,3):
                                instanciador[fila][columna+1].value(1)
                                instanciador[2][0].value(1)
                                instanciador[2][5].value(1)
                                sleep(0.2)
                                instanciador[2][0].value(0)
                                instanciador[2][5].value(0)
                                instanciador[fila][columna+1].value(0)
                                sleep(0.2)
                            manzana.value(0)
                            animacion()
                            serpiente()
                        while(botonW.value()==1 and botonS.value()==1 and a<=velocidad):
                            if(subir.value()==0):
                                velocidad=velocidad-2
                            if(bajar.value()==0):  
                                velocidad=velocidad+2                                
                            if(puntaje==1):
                                sleep(0.05)
                            else:
                                sleep(0.2)
                            a=a+1
                        a=0
                        puntaje=0
   
        if (botonW.value()==0):
            if(manzanaSpawn==0):
                while True:
                    manzana=instanciador[random.randint(1,4)][random.randint(1,4)]
                    if(manzana not in anaconda):
                        manzana.value(1)
                        manzanaSpawn=1
                        break            
            while (fila<6 and botonD.value()==1 and botonA.value()==1):
                    fila=fila-1
                    if(instanciador[fila][columna]==manzana):
                        puntaje=1
                        manzanaSpawn=0
                    if(fila>=1 and fila<5  ):
                        instanciador[fila][columna].value(1)
                        anaconda.insert(0,instanciador[fila][columna])
                    if(fila<5 ):
                        if(puntaje==0):
                            anaconda[len(anaconda)-1].value(0)
                            anaconda.pop(len(anaconda)-1)                        
                       
                        if(fila==0 or instanciador[fila][columna] in anaconda[1:len(anaconda)]):
                            for x in range(0,3):
                                instanciador[fila+1][columna].value(1)
                                instanciador[2][0].value(1)
                                instanciador[2][5].value(1)
                                sleep(0.2)
                                instanciador[2][0].value(0)
                                instanciador[2][5].value(0)
                                instanciador[fila+1][columna].value(0)
                                sleep(0.2)
                            manzana.value(0)
                            animacion()
                            serpiente()
                           
                        while(botonD.value()==1 and botonA.value()==1 and a<=velocidad):
                            if(subir.value()==0):
                                velocidad=velocidad-2
                            if(bajar.value()==0):  
                                velocidad=velocidad+2                                
                            if(puntaje==1):
                                sleep(0.05)
                            else:
                                sleep(0.2)
                            a=a+1
                        a=0
                        puntaje=0

                   
animacion()
serpiente()