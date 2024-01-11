import subprocess
from tkinter import Tk, Button
import tkinter as tk

from MLGUI import MLGUI


class First_Page(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="lightblue")
        self.root = root
        self.controller = controller
        menu_bar = tk.Menu(root)
        #root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Data Creation Page", command=lambda: self.controller.show_create_data())
        file_menu.add_command(label="Data Import Page", command=lambda: subprocess.run(["python", 'ImporterData.py']))
        file_menu.add_command(label="Exit", command=root.destroy)

        data_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Data", menu=data_menu)
        data_menu.add_command(label="Data Visualization Page", command=lambda: self.controller.Rep_data())
        data_menu.add_command(label="Machine Learning Page", command=lambda: self.controller.show_ml_gui())

        # Create buttons using pack layout
        button1 = Button(self, text="Créer les données", fg='#24baa3', bg='#197069',
                         command=lambda: self.controller.show_create_data())
        button1.bind('<Enter>', lambda e: button1.config(background='#24baa3', foreground='#197069'))
        button1.bind('<Leave>', lambda e: button1.config(background='#197069', foreground='#24baa3'))
        button1.pack(fill="x")

        button2 = Button(self, text="Importer un fichier des données", fg='#24baa3', bg='#197069',
                         command=lambda: subprocess.run(["python", 'ImporterData.py']))
        button2.bind('<Enter>', lambda e: button2.config(background='#24baa3', foreground='#197069'))
        button2.bind('<Leave>', lambda e: button2.config(background='#197069', foreground='#24baa3'))
        button2.pack(fill="x")

        button3 = Button(self, text="Algorithmes de machine learning", fg='#24baa3', bg='#197069',
                         command=lambda: self.controller.show_ml_gui())
        button3.bind('<Enter>', lambda e: button3.config(background='#24baa3', foreground='#197069'))
        button3.bind('<Leave>', lambda e: button3.config(background='#197069', foreground='#24baa3'))
        button3.pack(fill="x")

        button4 = Button(self, text="Représentation des Données", fg='#24baa3', bg='#197069',
                         command=lambda: self.controller.show_data_visualization())
        button4.bind('<Enter>', lambda e: button4.config(background='#24baa3', foreground='#197069'))
        button4.bind('<Leave>', lambda e: button4.config(background='#197069', foreground='#24baa3'))
        button4.pack(fill="x")

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
if __name__ == "__main__":
    root = Tk()
    app = First_Page(root, None)
    root.mainloop()
