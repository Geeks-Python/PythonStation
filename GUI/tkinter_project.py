from tkinter import *
import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk
from controller.subwaycontroller.main import runall
from tkinter import filedialog, Text
from tkinter import PhotoImage
import os
str1=os.getcwd()

window = tk.Tk()

def runApps():
            apps = [rf"{str1}\Car_Game\Game_code\car_game.exe",rf"{str1}\controller\car controller\controller.pyw"]
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

btn1 = tk.Button(text='subwaycontroller', command=runall, font=("arial 20"))
btn1.pack(pady=4)

btn = tk.Button(text='start car game !', command=runApps, font=("arial 20"))
btn.pack(pady=3)

btn.place(x=180, y=500)
btn1.place(x=420, y=500)



window.mainloop()

