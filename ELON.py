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


# Write your program here.
ev3.speaker.beep()
# Create your objects here.
ev3 = EV3Brick()
mi=Motor(Port.D)
md=Motor(Port.A)
si=ColorSensor(Port.S2)
sd=ColorSensor(Port.S1)

# Write your program here.
ev3.speaker.beep()
def colorA(): 
    global intensidadA 
    intensidadA= si.rgb()[1]
    if 1<=intensidadA <=9:
        return "negro"
    elif 10<=intensidadA<=16:
        return "gris"
    elif 17<=intensidadA <=20:
        return "verde"
    elif intensidadA > 35:
        return"blanco"
def colorB():                    
    global intensidadB
    intensidadB = sd.rgb()[1]
    if 1<=intensidadB <11:
        return "negro"
    elif 11<=intensidadB<=16:
        return "gris"
    elif 17<=intensidadB <=30:
        return "verde"
    elif intensidadB > 35:
        return "blanco"

def SEGUIDOR():
    if colorB()=="blanco":
        md.run(100)
    elif colorB()=="negro":
        md.run(-100)
    if colorA()=="blanco":
        mi.run(100)
    elif colorA()=="negro":
        mi.run(-100)
def CRUZ():
    if si.color()==Color.BLACK and sd.color()==Color.BLACK:   
        mi.stop()
        md.stop()
        mi.run_time(100,1500,then=Stop.HOLD,wait=False)
        md.run_time(100,1500,then=Stop.HOLD,wait=True)  
def VERDEi():
    if si.color()==Color.GREEN:
        mi.stop()
        md.stop()
        if colorA()=="verde":
            mi.stop()
            md.run(30)
            if colorB()=="verde":
                mi.run_time(-100,4000,then=Stop.HOLD,wait=False)
                md.run_time(100,4000,then=Stop.HOLD,wait=True)
                while sd.color()!=Color.BLACK:
                    mi.run(-100)
                    md.run(100)
            else:
                mi.run_time(100,1000,then=Stop.HOLD,wait=False)
                md.run_time(100,1000,then=Stop.HOLD,wait=True)
                mi.run_time(-100,1700,then=Stop.HOLD,wait=False)
                md.run_time(100,1700,then=Stop.HOLD,wait=True)
                while sd.color()!=Color.BLACK:
                    mi.run(-100)
                    md.run(100)
def VERDEd():
    if sd.color()==Color.GREEN:
        md.stop()
        mi.stop()
        if colorA()=="verde":
            md.stop()
            mi.run(30)
            if colorB()=="verde":
                md.run_time(-100,4000,then=Stop.HOLD,wait=False)
                mi.run_time(100,4000,then=Stop.HOLD,wait=True)
                while si.color()!=Color.BLACK:
                    md.run(-100)
                    mi.run(100)
            else:
                mi.run_time(100,1000,then=Stop.HOLD,wait=False)
                md.run_time(100,1000,then=Stop.HOLD,wait=True)
                md.run_time(-100,1650,then=Stop.HOLD,wait=False)
                mi.run_time(100,1650,then=Stop.HOLD,wait=True)
                while si.color()!=Color.BLACK:
                    md.run(-100)
                    mi.run(100)


while True:
    ev3.screen.print(str(sd.rgb()[1])+"  "+str(si.rgb()[1]),sep='')
    SEGUIDOR()
    #CRUZ()
    VERDEi()
    VERDEd()
    #COLOR()
