import pygame
import PySimpleGUI as sg
import time
import math

background_color=(255,255,255)
screen=pygame.display.set_mode((1200, 800))

pygame.display.set_caption("Drill")
screen.fill(background_color)

def draw_square(x,y,w,h,c):
    pygame.draw.rect(screen, c, pygame.Rect(x,y,w,h))

def draw_circle(x,y,r,c):
    pygame.draw.circle(screen, c, (x,y), r)

#for buttons to work, they HAVE to be in the list
Buttons=[]
class Button(object):
    def __init__(self,x,y,w,h,onclick):
        self.x=x
        self.y=y
        self.x2=x+w
        self.y2=y+h
        self.onclick=onclick
        
Marchers=[]
class Marcher(object):
    def __init__(self,x,y,group):
        self.x=x
        self.y=y
        self.group=group

Sets=[]

def prompt(promptText):
    layout = [[sg.Text(promptText)], [sg.Input()], [sg.Button("OK")]]
    window=sg.Window("PROMPT",layout)
    while True:
        event,values=window.read()
        if event=="OK" or event==sg.WIN_CLOSED:
            break
        time.sleep(0.01)
    window.close()
    
def alert(alertText):
    layout=[[sg.Text(alertText)],[sg.Button("OK")]]
    window=sg.Window("ALERT",layout)
    while True:
        event,values=window.read()
        if event=="OK" or event==sg.WIN_CLOSED:
            break
        time.sleep(0.01)
    window.close()
running=True
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
pygame.display.flip()

#prompt("How are you?")
#alert("BOO")
floor=True
while running:
    #pygame.draw.line(screen,(0,0,0),(600,0),(600,800))
    screen.fill(background_color)
    
    #sideline to home hash
    for i in range(22):
        pygame.draw.line(screen,(0,0,0),(0,175+(25*i)),(1200,175+(25*i)))
    
    #50yd to 35 side B
    for i in range(24):
        pygame.draw.line(screen,(0,0,0),(600+(25*i),175),(600+(25*i),700))
    
    #50 to 35 side A
    for i in range(24):
        pygame.draw.line(screen,(0,0,0),(600-(25*i),175),(600-(25*i),700))
    
    if len(Marchers)>0:
        for i in range(len(Marchers)):
            draw_circle(Marchers[i].x,Marchers[i].y,6,(0,255,0))
    
    #50yd line
    draw_circle(600,725,10,(255,0,0))
    
    #45yd
    draw_circle(400,725,7,(255,0,0))
    draw_circle(800,725,7,(255,0,0))
    
    #40yd
    draw_circle(200,725,5,(255,0,0))
    draw_circle(1000,725,5,(255,0,0))
    
    #35yd
    draw_circle(0,725,2,(255,0,0))
    draw_circle(1200,725,2,(255,0,0))
    
    mx,my=pygame.mouse.get_pos()
    mx_grid=math.ceil(mx/25)*25
    my_grid=math.ceil(my/25)*25
    
    if my<175:
        my_grid=175
    if my>700:
        my_grid=700
    
    draw_circle(mx_grid,my_grid,5,(0,0,255))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONUP:
            mx,my=pygame.mouse.get_pos()
            mx_grid=math.ceil(mx/25)*25
            my_grid=math.ceil(my/25)*25
            alert("A new marcher has entered the battle!")
            Marchers.append(Marcher(mx_grid,my_grid,"a"))
            
    pygame.display.flip()
pygame.quit()