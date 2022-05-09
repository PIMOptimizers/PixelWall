from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("900x500")
window.configure(bg = "#0E2433")
window.iconbitmap(r'pw22_EoA_icon.ico')
logo = PhotoImage(file=ASSETS_PATH / "logo.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Pixel Wall")

canvas = Canvas(
    window,
    bg = "#0E2433",
    height = 500,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("LevelUpImg.png"))
image_1 = canvas.create_image(
    450.0,
    250.0,
    image=image_image_1
)
window.after(3000, window.destroy)
window.resizable(False, False)
window.mainloop()
