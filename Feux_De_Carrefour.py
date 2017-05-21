#!/usr/bin/python
# -*- coding: cp1252 -*-
 
 
from Tkinter import *
import time
def start():
    
    if can1.itemcget(led2, 'fill') == 'orange':
        can1.itemconfigure(led1, fill = 'red')
        can1.itemconfigure(led2, fill = 'white')
        can1.itemconfigure(led3, fill = 'white')
        time.sleep(0.5)
    elif can1.itemcget(led3, 'fill') == 'green':
        can1.itemconfigure(led1, fill = 'white')
        can1.itemconfigure(led2, fill = 'orange')
        can1.itemconfigure(led3, fill = 'white')
        time.sleep(2)
    elif can1.itemcget(led1, 'fill') == 'red':
        can1.itemconfigure(led1, fill = 'white')
        can1.itemconfigure(led2, fill = 'white')
        can1.itemconfigure(led3, fill = 'green')
        time.sleep(2)
    
    root.after(1500, start)
 
root=Tk()
root.title("Exercice d'animation avec Tkinter")
can1 = Canvas(root, bg='dark grey',height=640,width=480)
feux=can1.create_rectangle(100,100,290,590,width=5,fill='black')
can1.pack(side=LEFT)
Button(root,text='Quitter',command=root.quit).pack(side=BOTTOM)
led1=can1.create_oval(125,125,250,250,width=5,fill='white')
led2=can1.create_oval(125,280,250,400,width=5,fill='white')
led3=can1.create_oval(125,405,250,530,width=5,fill='white')
can1.itemconfigure(led1, fill = 'red')
start()
root.mainloop()
