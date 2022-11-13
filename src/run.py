import include
import templates
import app

from tkinter import *


def set_window(TApp, extractor, name):
    TApp = TApp.replace('my_width', str(extractor.window_width)).replace('my_height', str(extractor.window_height)).replace('app_name', name)

    return TApp

def add_btn(TApp, btn):
    
    TApp = TApp + btn

    return TApp

def create_all_btns(TApp, btns_params):

    for btn in btns_params:
        TApp = add_btn(TApp, btn.generate_btn())

    return TApp

def add_entry(TApp, entry):
    TApp = TApp + entry

    return TApp

def create_all_entrys(TApp, entrys_params):
    for entry in entrys_params:
        TApp = add_entry(TApp, entry.generate_entry())

    return TApp

def create_run_file(name, width, height):
    TRun = templates.run_template.replace('my_name', name).replace('my_width', str(width)).replace('my_height', str(height))
    return TRun

def get_app(name, URL, token, path):
    extractor = include.extractor(URL, token, path)
    TApp = templates.app_template
    TApp = set_window(TApp, extractor, name)
    btns_data, entrys_data = extractor.get_data()

    btns_params = [include.CBtn(btn) for btn in btns_data]
    entrys_params = [include.CEntry(entry) for entry in entrys_data]

    TApp = create_all_btns(TApp, btns_params)
    TApp = create_all_entrys(TApp, entrys_params)
    
    TRun = create_run_file(name, extractor.window_width, extractor.window_height)

    return TApp, TRun



def run():
    #src.getMails()

    root = Tk()
    root.resizable(False, False)
    #Toma Icono de expeditos
    root.iconbitmap('./resources/favicon.ico')
    root.wm_title("Project_Generaton v1.0.0")

    #Crea ventana
    my_app = app.Project_Generator(root)
    #Da tamaño
    my_app.master.maxsize(800, 450)    
    my_app.mainloop()