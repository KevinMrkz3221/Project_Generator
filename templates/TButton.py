button_template = """
        #Button my_name
        self.my_name_img = PhotoImage(file="my_path")
        self.my_name_btn = Button(self,image=self.my_name_img, borderwidth = 0, highlightthickness = 0, relief = "flat", command=self.click)
        self.my_name_btn.place(x=my_x, y=my_y)
"""