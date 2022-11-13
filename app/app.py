
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkinter import *

#import pandas as pd

#import src
#import include

class Project_Generator(Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master, height=450, width=800)
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
        self.canvas1 = Canvas(self, bg='white',height=450, width=800)
        
        #Mandar llamar fondo de ventana
        self.background_img = PhotoImage(file="./resources/background.png")
        self.background = Label(self, image=self.background_img)
        self.background.place(x=0, y=0)


        #Button btnGetproject
        self.btnGetproject_img = PhotoImage(file="./resources/btnGetproject.png")
        self.btnGetproject_btn = Button(self,image=self.btnGetproject_img, borderwidth = 0, highlightthickness = 0, relief = "flat", command=self.click)
        self.btnGetproject_btn.place(x=465, y=385)

        #Button btnPath
        self.btnPath_img = PhotoImage(file="./resources/btnPath.png")
        self.btnPath_btn = Button(self,image=self.btnPath_img, borderwidth = 0, highlightthickness = 0, relief = "flat", command=self.click)
        self.btnPath_btn.place(x=718, y=73)

        #entryPath
        self.entryPath = Entry(self, bg='#eceeee', highlightthickness=0, bd=0)
        self.entryPath.place(x = 420, y = 72, width=274, height=28)

        #entryProject
        self.entryProject = Entry(self, bg='#eceeee', highlightthickness=0, bd=0)
        self.entryProject.place(x = 421, y = 198, width=274, height=28)

        #entryURL
        self.entryURL = Entry(self, bg='#eceeee', highlightthickness=0, bd=0)
        self.entryURL.place(x = 420, y = 264, width=274, height=28)

        #entryToken
        self.entryToken = Entry(self, bg='#eceeee', highlightthickness=0, bd=0)
        self.entryToken.place(x = 420, y = 330, width=274, height=28)
