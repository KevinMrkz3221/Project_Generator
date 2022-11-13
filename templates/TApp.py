
app_template = """
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkinter import *

#import pandas as pd

#import src
#import include

class app_name(Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master, height=my_height, width=my_width)
        self.master = master
        self.pack()

        #Se crea ventana
        self.create_widgets()
    

    def click(self):
        print('click')

    def Save_As(self):
        files = [('Excel Document', '*.xlsx'),
                ('CSV', '*.csv'),
                ('All Files', '*.*')
                ]
        folder_selected = filedialog.asksaveasfile(filetypes=files, defaultextension= files)

        # df = pd.DataFrame.from_records(self.registros)
        # if '.csv' in folder_selected.name:
        #     df.to_csv(folder_selected.name)
        # if '.xlsx' in folder_selected.name:
        #     df.to_excel(folder_selected.name)

    def create_widgets(self):
        self.canvas1 = Canvas(self, bg='white',height=my_height, width=my_width)
        
        #Mandar llamar fondo de ventana
        self.background_img = PhotoImage(file="./resources/background.png")
        self.background = Label(self, image=self.background_img)
        self.background.place(x=0, y=0)

"""