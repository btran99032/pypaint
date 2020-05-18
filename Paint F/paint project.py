from pygame import *
from math import*
from random import*
from tkinter import*
from tkinter import filedialog

width,height=800,600
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
BACK=[]
STAMPS=[image.load("images/s"+str(i)+".png")for i in range(1,9)]
BACK=[ image.load("back/b"+str(i)+".jpg")for i in range(1,6 )]










running=True

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
      
   
    display.flip()
            
quit()
