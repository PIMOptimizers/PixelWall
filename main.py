import os
from pprint import pprint
from tkinter import *
from pathlib import Path
import tkinter.font as font
from pymongo import MongoClient
import sys
#Games

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

def showChooseGamePage():
    window.destroy()
    os.system("python ChooseGamePage.py")
def showLoginPage():
    window.destroy()
    os.system("python LoginPage.py")
def showProfilPage():
    window.destroy()
    os.system("python ProfilePage.py")
def showLeaderBoardPage():
    window.destroy()
    os.system("python LeaderBoardPage.py")

#def showHomePage():
window = Tk()

window.geometry("1200x800")
window.configure(bg="#0E2433")
window.title('Pixell Wall by Optimizers')
window.iconbitmap(r'pw22_EoA_icon.ico')
logo = PhotoImage(file=ASSETS_PATH / "logo.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Pixel Wall")




# file handling
f = open("username.txt", "r")
username = f.read()
f.close()
print(username)

avatar = db.users.find_one({"username": username})['avatar']
score = db.users.find_one({"username": username})['score']


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
button_image_1 = PhotoImage(
    file=relative_to_assets("viewLeadeBoardBtn.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    command=showLeaderBoardPage,
    highlightthickness=0,
    relief="flat",
    activebackground='#0E2433'
)
button_1.place(
    x=387.0,
    y=488.0,
    width=400,
    height=87.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("HomeScore.png"))
image_2 = canvas.create_image(
    120.0,
    110.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("HomePlayBtn.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=showChooseGamePage,
    relief="flat",
    activebackground='#0E2433'
)
button_2.place(
    x=432.0,
    y=325.0,
    width=310.0,
    height=97.0
)
button_image_22 = PhotoImage(
    file=relative_to_assets(avatar))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=showProfilPage,
    relief="flat",
    activebackground='#0E2433'
)
button_22.place(
    x=850.0,
    y=14.0,
    width=109.72418212890625,
    height=99.43751525878906
)

image_image_3 = PhotoImage(
    file=relative_to_assets("backPixelHome.png"))
image_3 = canvas.create_image(
    600.0,
    420.0,
    image=image_image_3
)
canvas.create_text(
    50.0,
    30.0,
    anchor="nw",
    font=font.Font(family="Fixedsys", size=25),
    text=str(score),
    fill="#FFFFFF"
)
canvas.create_text(
    976.0,
    45.0,
    anchor="nw",
    text=username,
    fill="#FFFFFF",
    font=font.Font(family="Fixedsys",size=25),
)
window.resizable(False, False)
window.mainloop()

