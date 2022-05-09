import os
import tkinter
from tkinter import  messagebox
from pathlib import Path
from tkinter import *

# db config
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://pim:pimpassword@cluster0.5yxrc.mongodb.net/DB-PIM?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.dbPim

users = db.users
# file handling
f = open("username.txt", "r")
username = f.read()
f.close()



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

if os.stat('score_file.txt').st_size != 0:
    score_file = open("score_file.txt", "r")
    score = score_file.read()

    score_file.close()
    db.users.update_one({"username": username}, {"$inc": {"score": int(score)}})
    f = open("score_file.txt", "w")
    f.close()
    totalScore=db.users.find_one({"username": username})['score']

    if (totalScore >= 200 and (totalScore-int(score))<= 200):
        os.system("python LevelUpPage.py")
        db.users.update_one({"username": username}, {"$set": {"level": 2}})
    elif (totalScore >= 600 and (totalScore-int(score))<= 600):
        os.system("python LevelUpPage.py")
        db.users.update_one({"username": username}, {"$set": {"level": 3}})
    elif (totalScore >= 1100 and (totalScore-int(score))<= 1100):
        os.system("python LevelUpPage.py")
        db.users.update_one({"username": username}, {"$set": {"level": 4}})
    elif (totalScore >= 2000 and (totalScore-int(score))<= 2000):
        os.system("python LevelUpPage.py")
        db.users.update_one({"username": username}, {"$set": {"level": 5}})
    elif (totalScore >= 3000 and (totalScore-int(score))<= 3000):
        os.system("python LevelUpPage.py")
        db.users.update_one({"username": username}, {"$set": {"level": 6}})
    elif (totalScore >= 5000 and (totalScore-int(score))<= 5000):
        os.system("python LevelUpPage.py")
        db.users.update_one({"username": username}, {"$set": {"level": 7}})
# back button function
def back():
    window.destroy()
    os.system("python main.py")

lockFlappy=True
lockpingpong = True
lockspace =True
locktetris=True

ImgFlappy="lockedBtn.png"
Imgpingpong ="lockedBtn.png"
Imgspace ="lockedBtn.png"
Imgtetris="lockedBtn.png"


level= db.users.find_one({"username": username})['level']

if level>=7:
    lockFlappy = False
    lockpingpong = False
    lockspace = False
    locktetris = False
    ImgFlappy = "fluppyBtn.png"
    Imgpingpong = "PingPongBtn.png"
    Imgspace = "spaceBtn.png"
    Imgtetris = "TetrisBtn.png"
elif level>=5:
    lockFlappy = False
    lockpingpong = False
    lockspace = False
    ImgFlappy = "fluppyBtn.png"
    Imgpingpong = "PingPongBtn.png"
    Imgspace = "spaceBtn.png"

elif level>=4:
    lockFlappy = False
    lockpingpong = False
    ImgFlappy = "fluppyBtn.png"
    Imgpingpong = "PingPongBtn.png"

elif level>=2:
    lockFlappy = False
    ImgFlappy = "fluppyBtn.png"
def redlightgreen():
    window.destroy()
    os.system('python redlightgreen.py')

def snake():
    window.destroy()
    os.system('python snake.py')

def spaceinvadors():
    if lockspace :
        tkinter.messagebox.showerror(
            title="Game locked!", message="You should reach level 5 to unlock this game !")
        return
    else:
        window.destroy()
        os.system('python Space+Hand.py')
def bubbles():
    window.destroy()
    os.system('python bubblePop.py')
def fluppy():
    if lockFlappy :
        tkinter.messagebox.showerror(
            title="Game locked!", message="You should reach level 2 to unlock this game !")
        return
    else:
        window.destroy()
        os.system('python flappyBird.py')
def pingPong():
    if lockpingpong :
        tkinter.messagebox.showerror(
            title="Game locked!", message="You should reach level 4 to unlock this game !")
        return
    else:
        window.destroy()
        os.system('python pingpong.py')
def tetris():
    if locktetris :
        tkinter.messagebox.showerror(
            title="Game locked!", message="You should reach level 7 to unlock this game !")
        return
    else:
        window.destroy()
        os.system('python tetris.py')

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
    file=relative_to_assets("backChooseGamePage.png"))
image_1 = canvas.create_image(
    606.0001220703125,
    404.8554439544678,
    image=image_image_1
)

button_image_7 = PhotoImage(
    file=relative_to_assets("RedGreenBtn.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=redlightgreen,
    relief="flat"
)
button_7.place(
    x=603.0,
    y=121.0,
    width=202.0,
    height=260.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets(Imgspace))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=spaceinvadors,
    relief="flat"
)
button_8.place(
    x=492.0,
    y=392.0,
    width=202.0,
    height=260.0
)

button_image_snake = PhotoImage(
    file=relative_to_assets("snakeBtn.png"))
button_snake = Button(
    image=button_image_snake,
    borderwidth=0,
    highlightthickness=0,
    command=snake,
    relief="flat"
)
button_snake.place(
    x=382.0,
    y=126.0,
    width=202.0,
    height=260.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("home-btn.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_4.place(
    x=1107.0,
    y=689.0,
    width=80.0,
    height=80.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("bubblePopBtn.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=bubbles,
    relief="flat"
)
button_1.place(
    x=162.0,
    y=125.0,
    width=202.0,
    height=260.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets(Imgpingpong))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=pingPong,
    relief="flat"
)
button_2.place(
    x=267.0,
    y=392.0,
    width=202.0,
    height=260.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets(Imgtetris))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=tetris,
    relief="flat"
)
button_3.place(
    x=721.0,
    y=392.0,
    width=202.0,
    height=260.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets(ImgFlappy))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=fluppy,
    relief="flat"
)
button_6.place(
    x=829.0,
    y=126.0,
    width=202.0,
    height=260.0
)

window.resizable(False, False)
window.mainloop()
