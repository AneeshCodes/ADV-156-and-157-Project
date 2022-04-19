# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:14:40 2022

@author: anees
"""

from tkinter import *
from PIL import ImageTk,Image
import random
root = Tk()
root.title("OS Application Project")
root.geometry("800x600")
root.configure(bg="yellow")

btnRed = ImageTk.PhotoImage(Image.open("button.png"))
blastoise = ImageTk.PhotoImage(Image.open("blastoise.jpg"))
charizard = ImageTk.PhotoImage(Image.open("charizard.png"))
eevee = ImageTk.PhotoImage(Image.open("eevee.png"))
garchomp = ImageTk.PhotoImage(Image.open("garchomp.jpeg"))
gyarados = ImageTk.PhotoImage(Image.open("gyarados.jpeg"))
lycanroc = ImageTk.PhotoImage(Image.open("lycanroc.jpeg"))

player1 = Label(root, text="Player 1:")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)
player1s = Label(root)
player1s.place(relx=0.1,rely=0.4,anchor=CENTER)

player2 = Label(root, text="Player 2:")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)
player2s = Label(root)
player2s.place(relx=0.9,rely=0.4,anchor=CENTER)

pokemon = [blastoise,charizard,eevee,garchomp,gyarados,lycanroc]
score = [10,20,30,40,50,60]

label = Label(root)
label.place(relx=0.5,rely=0.5,anchor=CENTER)

p1s = 0

def player1():
    global p1s
    random_no = random.randint(0,5)
    random_pokemon = pokemon[random_no]
    label["image"] = random_pokemon
    random_score = score[random_no]
    p1s = p1s + random_score
    player1s["text"] = str(p1s)
    
    
p2s = 0

def player2():
    global p2s
    random_no2 = random.randint(0,5)
    random_pokemon2 = pokemon[random_no2]
    label["image"] = random_pokemon2
    random_score2 = score[random_no2]
    p2s = p2s + random_score2
    player2s["text"] = str(p2s)
    
p1btn = Button(root,height=30,width=30,image=btnRed,command=player1)
p1btn.place(relx=0.1,rely=0.6,anchor=CENTER)
p2btn = Button(root,height=30,width=30,image=btnRed,command=player2)
p2btn.place(relx=0.9,rely=0.6,anchor=CENTER)

root.mainloop()