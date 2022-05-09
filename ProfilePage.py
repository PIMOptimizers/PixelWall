
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter.font as font
from pprint import pprint
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

from pymongo import MongoClient

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def showEditProfilePage():
    window.destroy()
    os.system("python EditProfilePage.py")
def logOut():
    res = messagebox.askyesno('Warning', 'Are you sure you want to logout? \n back to grown ups life :(')
    if res == True:
        f = open("username.txt", "w")
        f.close()
        window.destroy()
        os.system("python LoginPage.py")

    elif res == False:
        pass

# db config
CONNECTION_STRING = "mongodb+srv://pim:pimpassword@cluster0.5yxrc.mongodb.net/DB-PIM?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.dbPim
pprint(db.list_collection_names())
users = db.users
# file handling
f = open("username.txt", "r")
username = f.read()
f.close()
print(username)

avatar = db.users.find_one({"username": username})['avatar']
level = db.users.find_one({"username": username})['level']
if (level==1):
    reward1 = "NoReward.png"
    reward2 = "NoReward.png"
    reward3 = "NoReward.png"
    reward4 = "NoReward.png"
    reward5 = "NoReward.png"
    reward6 = "NoReward.png"


elif(level==2):
    reward1 = "reward1.png"
    reward2 = "NoReward.png"
    reward3 = "NoReward.png"
    reward4 = "NoReward.png"
    reward5 = "NoReward.png"
    reward6 = "NoReward.png"
    reward7 = "NoReward.png"
elif(level==3):
    reward1 = "reward1.png"
    reward2 = "reward2.png"
    reward3 = "NoReward.png"
    reward4 = "NoReward.png"
    reward5 = "NoReward.png"
    reward6 = "NoReward.png"

elif(level==4):
    reward1 = "reward1.png"
    reward2 = "reward2.png"
    reward3 = "reward3.png"
    reward4 = "NoReward.png"
    reward5 = "NoReward.png"
    reward6 = "NoReward.png"

elif(level==5):
    reward1 = "reward1.png"
    reward2 = "reward2.png"
    reward3 = "reward3.png"
    reward4 = "reward4.png"
    reward5 = "NoReward.png"
    reward6 = "NoReward.png"

elif(level==6):
    reward1 = "reward1.png"
    reward2 = "reward2.png"
    reward3 = "reward3.png"
    reward4 = "reward4.png"
    reward5 = "reward5.png"
    reward6 = "NoReward.png"

elif(level==7):
    reward1 = "reward1.png"
    reward2 = "reward2.png"
    reward3 = "reward3.png"
    reward4 = "reward4.png"
    reward5 = "reward5.png"
    reward6 = "reward6.png"





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
    file=relative_to_assets("backProfilePage.png"))
image_1 = canvas.create_image(
    600.0,
    415.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(avatar))
image_2 = canvas.create_image(
    176.8191146850586,
    180.86346435546875,
    image=image_image_2
)

canvas.create_text(
    560.0,
    76.0,
    anchor="nw",
    text=username,
    fill="#FFFFFF",
    font=font.Font(family="Fixedsys",size=25)
)

canvas.create_text(
    543.0,
    163.0,
    anchor="nw",
    text="Level : "+str(level),
    font=font.Font(family="Fixedsys",size=25),
    fill="#FFFFFF"
)

image_image_3 = PhotoImage(
    file=relative_to_assets(reward1))
image_3 = canvas.create_image(
    456.2650146484375,
    386.2730407714844,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets(reward2))
image_4 = canvas.create_image(
    648.0,
    379.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(reward3))
image_5 = canvas.create_image(
    837.532958984375,
    385.2729797363281,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(reward4))
image_6 = canvas.create_image(
    457.4527893066406,
    521.1745910644531,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(reward5))
image_7 = canvas.create_image(
    649.1878051757812,
    517.4648132324219,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets(reward6))
image_8 = canvas.create_image(
    840.1533813476562,
    519.8643188476562,
    image=image_image_8
)

button_image_1 = PhotoImage(
    file=relative_to_assets("home-btn.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_1.place(
    x=1100.0,
    y=693.0,
    width=80.0,
    height=80.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("editProfileBtn.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=showEditProfilePage,
    relief="flat"
)
button_2.place(
    x=1071.0,
    y=33.0,
    width=92.0,
    height=87.0
)
#####
button_logout = PhotoImage(
    file=relative_to_assets("logoutBtn.png"))
button_logOut = Button(
    image=button_logout,
    borderwidth=0,
    highlightthickness=0,
    command=logOut,
    relief="flat"
)
button_logOut.place(
    x=33.0,
    y=682.0,
    width=80.0,
    height=80.0
)

window.resizable(False, False)
window.mainloop()
