from pathlib import Path
from pymongo import MongoClient
import tkinter as tk
import  os
import tkinter.font as font

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# db config
CONNECTION_STRING = "mongodb+srv://pim:pimpassword@cluster0.5yxrc.mongodb.net/DB-PIM?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.dbPim
users = db.users

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def showRegisterPage():
    window.destroy()
    os.system("python RegisterPage.py")
def showMain():
    window.destroy()
    os.system("python main.py")

def login():

    passw = entry_1.get()

    username = entry_2.get()

    if  db.users.find_one({"username" :username,"password":passw}) != None:

        # file handling
        f= open("username.txt","w")
        f.write(username)
        f.close()

        showMain()
    else:
        tk.messagebox.showinfo(
            "incorrect data!", "incorrect username or password !")
window = Tk()

window.geometry("1200x800")
window.configure(bg = "#0E2433")
logo = tk.PhotoImage(file=ASSETS_PATH / "logo.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Pixel Wall")

canvas = Canvas(
    window,
    bg = "#0E2433",
    height = 800,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("login-back-img.png"))
image_1 = canvas.create_image(
    600.0,
    443.0,
    image=image_image_1
)


button_image_2 = PhotoImage(
    file=relative_to_assets("login-login-btn.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_2.place(
    x=504.0,
    y=504.0,
    width=185.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("login-register-btn.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=showRegisterPage,
    relief="flat"
)
button_3.place(
    x=640.0,
    y=582.0,
    width=192.0,
    height=24.0
)



entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    753.0,
    320.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    font=font.Font(family="Fixedsys", size=20),
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=550.0,
    y=300.0,
    width=406.0,
    height=39.0
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    753.0,
    408.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    font=font.Font(family="Fixedsys",size=20),
    highlightthickness=0,
    show="*"
)
entry_1.place(
    x=550.0,
    y=388.0,
    width=406.0,
    height=39.0
)
entry_2.focus()

window.resizable(False, False)
window.mainloop()
