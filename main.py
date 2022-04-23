import os
from tkinter import *
from pathlib import Path
import sys
#Games


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def showChooseGamePage():
    window.destroy()
    os.system("python ChooseGamePage.py")


#def showHomePage():
window = Tk()

window.geometry("1200x800")
window.configure(bg="#0E2433")




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
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=387.0,
    y=488.0,
    width=393.6991882324219,
    height=86.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("UserNameHome.png"))
image_1 = canvas.create_image(
    1064.0,
    43.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("HomeScore.png"))
image_2 = canvas.create_image(
    103.0,
    84.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("HomePlayBtn.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=showChooseGamePage,
    relief="flat"
)
button_2.place(
    x=432.0,
    y=325.0,
    width=303.0,
    height=96.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("buttomPixelBlock.png"))
image_3 = canvas.create_image(
    600.0,
    672.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()

#showHomePage()

#main screen
def main_screen():
    global main_screen
    screen = Tk()
    screen.geometry("1300x700")
    screen.title("Pixel Wall")
    bg = PhotoImage(file="PW22.png")

    # Show image using label
    #label1 = Label(screen, image=bg)
    #label1.place(x=0, y=0)

    Label(text="Pixel Wall", bg="grey", width="300", font=("Calibri", 13)).pack()

    # Add buttons
    button1 = Button(screen, text="Game1", command=snake)
    button1.pack(pady=20)

    button2 = Button(screen, text="Game2", command=redlightgreen)
    button2.pack(pady=20)

    button3 = Button(screen, text="Game3", command=spaceinvadors)
    button3.pack(pady=20)

    #EXIT
    button3 = Button(screen, text="EXIT")
    button3.pack(pady=20)

    screen.mainloop()


#main_screen()
