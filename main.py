import os
import tkinter as tk

from Controller import Controller
from First_Page import First_Page


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.controller = Controller(self)

    def destroy(self):
        # Delete the file on closing the app
        try:
            # Obtenir le répertoire courant
            current_directory = os.getcwd()
            destination_path = os.path.join(current_directory, "data")
            os.remove(destination_path)
        except FileNotFoundError:
            pass
        super().destroy()



if __name__ == "__main__":
    main = Main()
    main.mainloop()
