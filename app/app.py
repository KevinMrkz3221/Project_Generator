
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkinter import *

import src


class Project_Generator(Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master, height=450, width=800)
        self.master = master
        self.pack()

        #Se crea ventana
        self.create_widgets()

    def create_project(self):
            path = self.entryPath.get()
            project_name = self.entryProject.get().replace('-', '_'). replace(' ','')
            URL = self.entryURL.get()
            token = self.entryToken.get()
            

            if messagebox.askyesno('Warning!', f'Project will be created at {path + project_name}.\n Do you want to continue?'):
                if not src.create_directories(path, project_name):
                    if messagebox.askyesno('Warning!', 'The project already exists, do you want to delete the old project?'):
                        src.create_directories(path, project_name, selector=1)
                        TApp, TRun = src.get_app(project_name, URL, token, path+project_name)
                        src.create_python_files(path, project_name, TApp, TRun)
                        messagebox.showinfo('Successfully!', 'Se creo el proyecto!')
                        
                else:
                    TApp, TRun = src.get_app(project_name, URL, token, path+project_name)
                    src.create_python_files(path, project_name, TApp, TRun)
                    messagebox.showinfo('Successfully!', 'Se creo el proyecto!')
            
            


    def get_path(self, *args):
        path = filedialog.askdirectory()
        if path:
            self.entryPath.delete(0, END)
            self.entryPath.insert(0, path+'/')

    def create_widgets(self):
        self.canvas1 = Canvas(self, bg='white',height=450, width=800)
        
        #Mandar llamar fondo de ventana
        self.background_img = PhotoImage(file="./resources/background.png")
        self.background = Label(self, image=self.background_img)
        self.background.place(x=0, y=0)


        #Button btnGetproject
        self.btnGetproject_img = PhotoImage(file="./resources/btnGetproject.png")
        self.btnGetproject_btn = Button(self,image=self.btnGetproject_img, borderwidth = 0, highlightthickness = 0, relief = "flat", command=self.create_project)
        self.btnGetproject_btn.place(x=465, y=385)

        #Button btnPath
        self.btnPath_img = PhotoImage(file="./resources/btnPath.png")
        self.btnPath_btn = Button(self,image=self.btnPath_img, borderwidth = 0, highlightthickness = 0, relief = "flat", command=self.get_path)
        self.btnPath_btn.place(x=718, y=73)

        #entryPath
        self.entryPath = Entry(self, bg='#eceeee', highlightthickness=0, bd=0)
        self.entryPath.place(x = 420, y = 72, width=274, height=28)
        self.entryPath.insert(0,'C:/')
        self.entryPath.bind("<1>", self.get_path)

        #entryProject
        self.entryProject = Entry(self, bg='#eceeee', highlightthickness=0, bd=0)
        self.entryProject.place(x = 421, y = 198, width=274, height=28)

        #entryURL
        self.entryURL = Entry(self, bg='#eceeee', highlightthickness=0, bd=0)
        self.entryURL.place(x = 420, y = 264, width=274, height=28)

        #entryToken
        self.entryToken = Entry(self, bg='#eceeee', highlightthickness=0, bd=0)
        self.entryToken.place(x = 420, y = 330, width=274, height=28)


