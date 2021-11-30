from tkinter import *
import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog, Text
from tkinter import PhotoImage
import os

window = tk.Tk()

def runApps():
    apps = [r"C:\Users\samki\PycharmProjects\PythonStation\Car_Game\Game_code\car_game.exe",r"C:\Users\samki\PycharmProjects\PythonStation\controller\controller.pyw"]
    for app  in apps:
        os.startfile(app)


CANVAS = tk.Canvas(window, height=600, width=600, bg="#263D62")
CANVAS.pack()

window.title('gameStaion')
window.geometry('800x650')
window.config(bg="white")
window.iconbitmap("favicon.ico")

pic = r"game.jpg"
pic1 = p.Image.open(pic)
photo = ptk.PhotoImage(pic1)




label1 = tk.Label(window, image=photo)


label1.place(x=0, y=0, relwidth=1, relheight=1)

btn = tk.Button(text='start game', command=runApps, font=("arial 20"))
btn.pack(pady=3)



window.mainloop()

