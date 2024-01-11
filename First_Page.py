import subprocess
from tkinter import Tk, Button
import tkinter as tk

from MLGUI import MLGUI


class First_Page(tk.Frame):
    def __init__(self, root,controller):
        super().__init__(root, bg="lightblue")
        self.root = root
        self.controller = controller
        # Create buttons directly in __init__
        button1 = Button(self, width=43, height=2, text="Créer les données", fg='#24baa3', bg='#197069',
                         border=0, command=lambda: subprocess.run(["python", 'createdata.py']))
        button1.bind('<Enter>', lambda e: button1.config(background='#24baa3', foreground='#197069'))
        button1.bind('<Leave>', lambda e: button1.config(background='#197069', foreground='#24baa3'))
        button1.place(x=0, y=0)

        button2 = Button(self, width=43, height=2, text="Importer un fichier des données", fg='#24baa3', bg='#197069',
                         border=0, command=lambda: subprocess.run(["python", 'ImporterData.py']))
        button2.bind('<Enter>', lambda e: button2.config(background='#24baa3', foreground='#197069'))
        button2.bind('<Leave>', lambda e: button2.config(background='#197069', foreground='#24baa3'))
        button2.place(x=0, y=37)

        button3 = Button(self, width=43, height=2, text="Algorithmes de machine learning", fg='#24baa3', bg='#197069',
                         border=0, command=lambda:self.controller.show_ml_gui())
        button3.bind('<Enter>', lambda e: button2.config(background='#24baa3', foreground='#197069'))
        button3.bind('<Leave>', lambda e: button2.config(background='#197069', foreground='#24baa3'))
        button3.place(x=0, y=74)

        button4 = Button(self, width=43, height=2, text="Gestion des données", fg='#24baa3', bg='#197069',
                         border=0, command=lambda: self.controller.show_data_manager_gui())
        button4.bind('<Enter>', lambda e: button2.config(background='#24baa3', foreground='#197069'))
        button4.bind('<Leave>', lambda e: button2.config(background='#197069', foreground='#24baa3'))
        button4.place(x=0, y=111)
        #self.create_button(0, 0, "Créer les données", '#24baa3', '#197069', 'createdata.py')
        #self.create_button(0, 37, "Importer un fichier des données", '#24baa3', '#197069', 'ImporterData.py')
        # self.create_button(0, 74, "Représnter les données", '#24baa3', '#197069', 'RepData.py')
        # self.create_button(0, 111, "Gestion des données", '#24baa3', '#197069', 'manageData.py')
        #self.create_button(0, 148, "Algorithmes de machine learning", '#24baa3', '#197069', 'MLGUI.py')
    def hide(self):
        self.pack_forget()



    def create_button(self, x, y, text, bcolor, fcolor, path):
        def on_enter(e):
            my_button['background'] = bcolor
            my_button['foreground'] = fcolor

        def on_leave(e):
            my_button['background'] = fcolor
            my_button['foreground'] = bcolor

        def on_click():
            # Run the external script when the button is clicked
            subprocess.run(["python", path])

        my_button = Button(self.root, width=43, height=2, text=text, fg=bcolor, bg=fcolor,
                           border=0, activebackground=bcolor, activeforeground=fcolor, command=on_click)
        my_button.bind('<Enter>', on_enter)
        my_button.bind('<Leave>', on_leave)
        my_button.place(x=x, y=y)


