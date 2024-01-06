import tkinter as tk
from createdata import CSVEditorApp
from First_Page import First_Page
from MLGUI import MLGUI
class Controller:
    def __init__(self, root):
        self.CSVEditorApp = None
        self.ml_gui = None
        self.first_page = None
        self.root = root
        self.root.title("Main")
        self.root.geometry("400x300")
        self.root.configure(bg="lightblue")
        self.show_first_page()

    def show_first_page(self):
        self.first_page = First_Page(self.root, self)
        self.first_page.pack(fill=tk.BOTH, expand=True)

    def show_ml_gui(self):
        self.ml_gui = MLGUI(self.root, self)
        self.ml_gui.pack(fill=tk.BOTH, expand=True)
        self.first_page.hide()
    def show_create_data(self):
        if self.first_page:
            self.first_page.hide()
        self.CSVEditorApp = CSVEditorApp(self.root, self)
        self.CSVEditorApp.pack(fill=tk.BOTH,expand=True)
        self.first_page.hide()