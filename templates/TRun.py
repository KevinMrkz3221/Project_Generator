run_template = """
from tkinter import *
import app

def frun():
    root = Tk()
    root.resizable(False, False)

    #Toma Icono de expeditos
    root.iconbitmap('./resources/favicon.ico')

    root.wm_title("my_name")

    #Crea ventana
    _app = app.my_name(root)

    #Da tamaño
    _app.master.maxsize(my_width, my_height)    

    _app.mainloop()
"""