import tkinter as tk

from First_Page import First_Page
from MLGUI import MLGUI
class Controller:
    def __init__(self, root):
        self.ml_gui = None
        self.first_page = None
        self.root = root
        self.root.title("Main")
        self.root.geometry("400x300")
        self.root.configure(bg="red")
        self.show_first_page()

    def show_first_page(self):
        self.first_page = First_Page(self.root, self)
        self.first_page.pack(fill=tk.BOTH, expand=True)

    def show_ml_gui(self):
        self.ml_gui = MLGUI(self.root, self)
        self.ml_gui.pack(fill=tk.BOTH, expand=True)
        self.first_page.hide()