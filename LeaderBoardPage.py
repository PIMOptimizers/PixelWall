import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pymongo import MongoClient

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
# db config
CONNECTION_STRING = "mongodb+srv://pim:pimpassword@cluster0.5yxrc.mongodb.net/DB-PIM?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.dbPim
users = db.users
L=db.users.find()
List=[]
for i in L:
    List.append((i['username'],i['score']))

List.sort(key=lambda a: a[1],reverse=True)
for i in range(len(List)):
    List[i]=(i+1,)+List[i]


def back():
    window.destroy()
    os.system("python main.py")


window = Tk()

window.geometry("1200x800")
window.configure(bg = "#0E2433")
window.title('Pixell Wall by Optimizers')
window.iconbitmap(r'pw22_EoA_icon.ico')
logo = PhotoImage(file=ASSETS_PATH / "logo.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Pixel Wall")

style= ttk.Style()
style.configure(
    "Treeview",
    rowheight=46,
    font=("Fixedsys", 20),
    #font=font.Font(family="Fixedsys",size=30,weight="bold"),
    foreground='#0E2433',
    background='#D1DBE1'
)
style.configure('RW.TLabel', background='#D1DBE1')
style.map('Treeview',
          background=[('selected','#D1DBE1')],
          foreground=[('selected','#0E2433')])
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
    file=relative_to_assets("backLeaderBoard.png"))
image_1 = canvas.create_image(
    600.0,
    423.0,
    image=image_image_1
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
    x=1071.0,
    y=686.0,
    width=80.0,
    height=80.0
)

# define columns
columns = ('rank', 'username', 'score')

tree = ttk.Treeview(window, columns=columns, show='',height=10)

tree.column('rank',width=43,anchor='center')
tree.column('score',width=100,anchor='center')
tree.column('username',width=803,anchor='center')

# add data to the treeview
for contact in  List:

    tree.insert('', tk.END,values=contact)


# add a scrollbar
scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview, style= 'RW.TLabel' )
tree.configure(yscroll=scrollbar.set)

scrollbar.place(x=1070, y=131, height=458)
tree.place(
    x=138,
    y=130
)
window.resizable(False, False)
window.mainloop()
