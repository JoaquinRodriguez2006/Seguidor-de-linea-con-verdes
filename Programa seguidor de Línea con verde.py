#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
mi=Motor(Port.B)
md=Motor(Port.C)
si=ColorSensor(Port.S1)
sd=ColorSensor(Port.S4)

# Write your program here.
ev3.speaker.beep()
def SEGUIDOR():
    #SEGUIDOR DE LÍNEA
    if sd.color()==Color.WHITE:
        md.run(150)
    elif sd.color()==Color.BLACK:
        md.run(-150)
    if si.color()==Color.WHITE:
        mi.run(150)
    elif si.color()==Color.BLACK:
        mi.run(-150)
    #Aumenté la velocidad del seguidor de 100 a 150 para más rapidez

def DETECCIÓN_COLOR():
    #ESTA FUNCIÓN DETECTA QUÉ COLOR SE ENCUENTRA EN EL PISO Y SE ACOMODA PARA COMPROBAR
    if si.color()==Color.GREEN:
        mi.stop()
        md.stop()
        if 21 <= si.rgb()[1]<=23:
            while sd.color!=Color.GREEN:
                mi.stop()
                md.run(100)
            if 20 <= sd.rgb()[1]<=22:
                md.run_time(100,1500,then=Stop.HOLD,wait=False)
                mi.run_time(-100,1500,then=Stop.HOLD,wait=True)
                #No sé si aquí no quedará atrás del verde. Al retroceder  con un motor y avanzar con el otro el mismo tiempo, puede
                #llegar a quedar un poco más atrás del VERDE, o por lo menos en la intersección entre VERDE y BLANCO
                while sd.color()!=Color.BLACK:
                    md.run(100)
                    mi.run(-100)
                #Con esto se podría solucionar. Avanza hasta que detecta el negro. 
        else: 
            mi.run(100)
            md.run(100)

def CRUZ():
    #ESTA FUNCIÓN DETECTA EL DOBLE NEGRO (CRUZ) Y LA SUPERA
    if 13 <= si.rgb()[1]<= 14 and 5 <= sd.rgb()[1]<= 9: #Falta comprobar valores
        mi.run_time(100,1000,then=Stop.HOLD,wait=False)
        md.run_time(100,1000,then=Stop.HOLD,wait=True)
        #Según nos dijo el profe, cambié este IF. Antes tenía instrucciones de hacer el RUN_TIME SI detectaba BLACK. Ahora 
        #cambié la detección de color por detección de reflejo de luz, para mayor presición
#
            

def VERDE():
    if si.color()==Color.GREEN:
        mi.stop()
        md.stop()
        if 22 <= si.rgb()[1]<= 24:
            mi.run_time(100,1100,then=Stop.HOLD,wait=False)
            md.run_time(100,500,then=Stop.HOLD,wait=True) 
            mi.run_time(-100,1100,then=Stop.HOLD,wait=False) 
            md.run_time(100,500,then=Stop.HOLD,wait=True) 
            while sd.color()!=Color.BLACK:
                mi.run(-100)
                md.run(100)
        else:
            mi.run(30)
            md.run(30)

    elif sd.color()==Color.GREEN:
        mi.stop()
        md.stop()
        if 22 <= sd.rgb()[1]<= 24:
            mi.run_time(100,1100,then=Stop.HOLD,wait=False)
            md.run_time(100,500,then=Stop.HOLD,wait=True)
            mi.run_time(100,1100,then=Stop.HOLD,wait=False)
            md.run_time(-100,500,then=Stop.HOLD,wait=True)
            while si.color()!=Color.BLACK:
                mi.run(100)
                md.run(-100)
        else: 
            mi.run(30)
            md.run(30)
    
    elif sd.color()==Color.GREEN and si.color()==Color.GREEN:
        mi.stop()
        md.stop()
        if 22 <= sd.rgb()[1]<= 24 and 31 <= si.rgb()[1]<= 33:
            mi.run_time(-100,1500,then=Stop.HOLD,wait=False)
            md.run_time(-100,1500,then=Stop.HOLD,wait=True)
            mi.run_time(100,1250,then=Stop.HOLD,wait=False)
            md.run_time(-100,1250,then=Stop.HOLD,wait=True)
            mi.stop()
            md.stop()
            mi.run_time(100,1050,then=Stop.HOLD,wait=False)
            md.run_time(100,1050,then=Stop.HOLD,wait=True)


#while True:
    #ev3.screen.print(sd.rgb()[1],sep='')
    #ev3.screen.print(si.rgb()[1],sep='')
while True:
    SEGUIDOR()
    CRUZ()
    VERDE()


