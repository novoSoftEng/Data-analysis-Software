import tkinter as tk
from First_Page import First_Page
from MLGUI import MLGUI
from DataManagerGUI import DataManagerGUI  # Import your DataManagerGUI class

class Controller:
    def __init__(self, root):
        self.ml_gui = None
        self.first_page = None
        self.data_manager_gui = None  # Add an instance of DataManagerGUI
        self.root = root
        self.root.title("Main")
        self.root.resizable(width=True, height=True)
        self.root.geometry("800x600")
        self.root.configure(bg="red")
        self.show_first_page()

    def show_first_page(self):
        self.first_page = First_Page(self.root, self)
        self.first_page.pack(fill=tk.BOTH, expand=True)

    def show_ml_gui(self):
        self.ml_gui = MLGUI(self.root, self)
        self.ml_gui.pack(fill=tk.BOTH, expand=True)
        self.first_page.hide()

    def show_data_manager_gui(self):
        if self.data_manager_gui is None:
            self.data_manager_gui = DataManagerGUI(self.root, self)
        self.data_manager_gui.pack(fill=tk.BOTH, expand=True)
        self.first_page.hide()

    def hide_data_manager_gui(self):
        if self.data_manager_gui:
            self.data_manager_gui.pack_forget()
        self.show_first_page()


