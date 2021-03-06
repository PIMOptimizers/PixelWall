import os
from pathlib import Path
import tkinter.font as font
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox

from pymongo import MongoClient

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1200x800")
window.configure(bg = "#0E2433")
window.title('Pixell Wall by Optimizers')
window.iconbitmap(r'pw22_EoA_icon.ico')
logo = PhotoImage(file=ASSETS_PATH / "logo.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Pixel Wall")

# db config
CONNECTION_STRING = "mongodb+srv://pim:pimpassword@cluster0.5yxrc.mongodb.net/DB-PIM?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.dbPim

users = db.users
# file handling
f = open("username.txt", "r")
username = f.read()
f.close()

newAvatar = db.users.find_one({"username": username})['avatar']
disabled = "disabled"


def setAvatar1():
    global newAvatar
    newAvatar="avatar1.png"
    return
def setAvatar2():
    global newAvatar
    newAvatar="avatar2.png"
    return
def setAvatar3():
    global newAvatar
    newAvatar="avatar3.png"
    return
def setAvatar4():
    global newAvatar
    newAvatar="avatar4.png"
    return
def setAvatar6():
    global newAvatar
    newAvatar="avatar6.png"
    return
def setAvatar5():
    global newAvatar
    newAvatar="avatar5.png"
    return

def verifPass():
    passw = entry_2.get()

    if (passw == ""):
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter your data")
        return
    elif db.users.count_documents({'username': username, 'password':passw}) == 0:
        tk.messagebox.showerror(
            title="Incorrect data!", message="Wrong password!")
        return
    else:
        global disabled
        disabled="normal"
        entry_3.config(state=disabled)
        return



def updateProfile():
    newUsername = entry_1.get()
    newpass = entry_3.get()
    global newAvatar
    if (disabled == "normal"):
        db.users.update_one({"username": username}, {"$set": {"password": newpass}})
    db.users.update_one({"username": username}, {"$set": {"avatar": newAvatar}})
    if (newUsername!= username):
        if db.users.count_documents({'username': newUsername}) != 0:
            tk.messagebox.showerror(
                title="Data error!", message="Username already in use !")
            return
        else:
            db.users.update_one({"username": username}, {"$set": {"username": newUsername}})

    # file handling
    f = open("username.txt", "w")
    f.write(newUsername)
    f.close()
    # page handling
    window.destroy()
    os.system("python ProfilePage.py")


def back():
    window.destroy()
    os.system("python main.py")

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
    file=relative_to_assets("backEditProfilePage.png"))
image_1 = canvas.create_image(
    600.0,
    431.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("home-btn.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat",
    activebackground='#0E2433'
)
button_1.place(
    x=1100.0,
    y=693.0,
    width=80.0,
    height=80.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("avatar2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=setAvatar2,
    relief="flat",
    activebackground='#0E2433'
)
button_2.place(
    x=300.0,
    y=200.0,
    width=100,
    height=100.0
)
button_verif = PhotoImage(
    file=relative_to_assets("verifBtn.png"))
button_verifP = Button(
    image=button_verif,
    borderwidth=0,
    highlightthickness=0,
    command=verifPass,
    relief="flat",
    activebackground='#0E2433'
)
button_verifP.place(
    x=1005.0,
    y=254.0,
    width=47.0,
    height=47.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("avatar1.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=setAvatar1,
    relief="flat",
    activebackground='#0E2433'
)
button_3.place(
    x=120.0,
    y=200.0,
    width=100,
    height=100.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("avatar3.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=setAvatar3,
    relief="flat",
    activebackground='#0E2433'
)
button_4.place(
    x=120.0,
    y=330.0,
    width=100,
    height=95.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("avatar4.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=setAvatar4,
    relief="flat",
    activebackground='#0E2433'
)
button_5.place(
    x=300.0,
    y=330.0,
    width=100,
    height=100.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("avatar5.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=setAvatar5,
    relief="flat",
    activebackground='#0E2433'
)
button_6.place(
    x=120.0,
    y=460.0,
    width=100,
    height=100.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("avatar6.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=setAvatar6,
    relief="flat",
    activebackground='#0E2433'
)
button_7.place(
    x=300.0,
    y=460.0,
    width=100,
    height=100.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    764.0,
    166.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=font.Font(family="Fixedsys",size=20)
)
entry_1.insert(0,username)
entry_1.place(
    x=561.0,
    y=146.0,
    width=410.0,
    height=41.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    764.0,
    274.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    show="*",
    font=font.Font(family="Fixedsys",size=20)
)
entry_2.place(
    x=561.0,
    y=254.0,
    width=410.0,
    height=41.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    764.0,
    350.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    show="*",
    font=font.Font(family="Fixedsys",size=20),
    highlightthickness=0
)

entry_3.place(
    x=561.0,
    y=330.0,
    width=410.0,
    height=41.0
)

entry_3.config(state=disabled)
button_image_8 = PhotoImage(
    file=relative_to_assets("savechangesBtn.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=updateProfile,
    relief="flat",
    activebackground='#0E2433'
)
button_8.place(
    x=549.0,
    y=454.0,
    width=435.0,
    height=75.0
)
entry_1.focus()
window.resizable(False, False)
window.mainloop()
