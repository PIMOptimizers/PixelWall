# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from pprint import pprint
from pymongo import MongoClient
import tkinter as tk
import  os
import tkinter.font as font
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

# db config
CONNECTION_STRING = "mongodb+srv://pim:pimpassword@cluster0.5yxrc.mongodb.net/DB-PIM?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.dbPim
pprint(db.list_collection_names())
users = db.users

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def LoginPage():
    window.destroy()
    os.system("python LoginPage.py")


cpass = tk.StringVar
passw = tk.StringVar
username = tk.StringVar


def register():
    cpass = entry_1.get()
    print("Cpass : " + cpass)
    passw = entry_2.get()
    print("Pass : " + passw)
    username = entry_3.get()
    print("username : " + username)

    if (passw == "" and cpass == "" and username == ""):
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter your data")
        return
    else:
        if (cpass == passw):
            if db.users.count_documents({'username': username}) == 0:
                user = {"username": username, "password": passw, "level": 1, "avatar": "avatar1.png", "score": 0}
                result = users.insert_one(user)
                tk.messagebox.showinfo(
                    "Success!", "Your account has benn created")
                LoginPage()


            else:
                tk.messagebox.showerror(
                    title="Data error!", message="Username already in use !")
                return
        else:
            tk.messagebox.showerror(
                title="Typing error!", message="Password and confirm password should be the same !")
            return


window = Tk()

window.geometry("1200x800")
window.configure(bg="#0E2433")
logo = tk.PhotoImage(file=ASSETS_PATH / "logo.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Pixel Wall")

canvas = Canvas(
    window,
    bg="#0E2433",
    height=800,
    width=1200,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("register-background.png"))
image_1 = canvas.create_image(
    600.0,
    435.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("register-username-entry.png"))
entry_bg_1 = canvas.create_image(
    753.0,
    419.5,
    image=entry_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("register-next-btn.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=register,
    relief="flat"
)

button_1.place(
    x=504.0,
    y=504.0,
    width=190.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("register-login-btn.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=LoginPage,
    relief="flat"
)
button_3.place(
    x=640.0,
    y=582.0,
    width=120.0,
    height=24.0
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    font=font.Font(family="Fixedsys", size=20),
    highlightthickness=0
)
entry_3.place(
    x=550.0,
    y=261.0,
    width=406.0,
    height=39.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("register-pass-entry.png"))
entry_bg_2 = canvas.create_image(
    753.0,
    350.5,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    font=font.Font(family="Fixedsys", size=20),
    bg="#FFFFFF",
    highlightthickness=0,
    show="*"
)

entry_2.place(
    x=550.0,
    y=330.0,
    width=406.0,
    height=39.0
)
entry_1 = tk.Entry(
    bd=0,
    bg="#FFFFFF",
    font=font.Font(family="Fixedsys", size=20),
    highlightthickness=0,
    show="*"
)
entry_1.place(
    x=550.0,
    y=399.0,
    width=406.0,
    height=39.0
)
entry_image_3 = PhotoImage(
    file=relative_to_assets("register-cpass-entry.png"))
entry_bg_3 = canvas.create_image(
    753.0,
    281.5,
    image=entry_image_3
)
entry_3.focus()
window.resizable(False, False)

window.mainloop()
