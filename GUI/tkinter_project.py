from tkinter import  *
import tkinter as tk
import  PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog,Text
from tkinter import PhotoImage
import os

window = tk.Tk()



# if os.path.isfile("saveApps.txt"):
#     with open("saveApps.txt","r") as saved:
#         tempApps = saved.read()
#         tempApps = tempApps.split(",")
#         apps= [x for x in tempApps if x.strip()]

# def browesFiles():
#     for widget in FRAME.winfo_children():
#         widget.destroy()
#
#     filename=filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("excutables","*.exe"),("all files","*,*")))
#     apps.append((filename))
#     print(filename)
#     for app in apps:
#         label=tk.Label(FRAME,text=app,bg="#263D89")
#         label.pack()


def runApps():
    apps = [r"C:\Users\STUDENT\Desktop\game\car-race-python-game-master\car-race-python-game-master\game.jpg",r"C:\Users\STUDENT\Desktop\game\car-race-python-game-master\car-race-python-game-master\online-games.jpg"]
    for app  in apps:
        os.startfile(app)

CANVAS= tk.Canvas(window,height = 600,width = 600,bg = "#263D62")
CANVAS.pack()

window.title('gameStaion')
window.geometry('800x650')
window.config(bg="white")
window.iconbitmap("favicon.ico")

pic=r"game.jpg"
pic1=p.Image.open(pic)
photo = ptk.PhotoImage(pic1)

# FRAME = tk.Frame(window,bg="#263D42")
# FRAME.place(relwidth = 0.9,relheight=0.8,relx=0.05,rely=0.05)

# browser = tk.Button(text='Browser',padx= 10 ,pady = 5,fg='white',bg="#196E63",border="0" ,command=browesFiles)
# browser.pack()

# Run = tk.Button(text='Run app',padx= 9 ,pady = 5,fg='white',bg="#196E63",border="0" ,command=runApps)
# Run.pack()


label1= tk.Label(window,image = photo)
#
# def open_game():
#     # my_promgram = filedialog.askopenfilename()
#     # my_label.config(text=my_promgram)
#     # os.system('"%s"' % my_promgram)
#     game= r'C:\Windows\notepad.exe'
#     image = r'C:\Users\STUDENT\Desktop\game\car-race-python-game-master\car-race-python-game-master\online-games.jpg'
#     os.system('"%s"' % game)
#     os.system('"%s"' % image)
#
#
# my_label=tk.Label(window,text='')
# # lbl = tk.Label(text='0',font=('arial bold',50))
# my_label.pack()


# my_text = tk.Label(text="Welcome!",font=('Helvetica',50),fg="white")
# my_text.pack(pady=50)

#
#
label1.place(x=0,y=0,relwidth=1,relheight=1)

btn = tk.Button(text='start game' ,command = runApps,font=("arial 20"))
btn.pack(pady = 3)


# for app in apps:
#     label=tk.Label(FRAME,text=app)
#     label.pack()

window.mainloop()

#
# with open("saveApps.txt","w") as saved :
#     for app in apps :
#         saved.write(app + ",")