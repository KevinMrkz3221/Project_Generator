
from tkinter import *
import app

def frun():
    root = Tk()
    root.resizable(False, False)

    #Toma Icono de expeditos
    root.iconbitmap('./resources/favicon.ico')

    root.wm_title("Project_Generator")

    #Crea ventana
    _app = app.Project_Generator(root)

    #Da tamaño
    _app.master.maxsize(800, 450)    

    _app.mainloop()
