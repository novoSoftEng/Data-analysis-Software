import subprocess
from tkinter import Tk, Button
import tkinter as tk
class First_Page(tk.Frame):
    def __init__(self, root):
        super().__init__(root, bg="lightblue")
        self.root = root
        self.root.geometry('300x148')
        self.root.configure(bg='#040c0c')

        self.create_button(0, 0, "Créer les données", '#24baa3', '#197069', 'createdata.py')
        self.create_button(0, 37, "Importer un fichier des données", '#24baa3', '#197069', 'ImporterData.py')
        # self.create_button(0, 74, "Représnter les données", '#24baa3', '#197069', 'RepData.py')
        # self.create_button(0, 111, "Gestion des données", '#24baa3', '#197069', 'manageData.py')
        # self.create_button(0, 148, "Algorithmes de machine learning", '#24baa3', '#197069', 'algo.py')

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


