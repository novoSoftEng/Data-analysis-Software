import tkinter as tk
from tkinter import ttk

from DataManager import DataManager
from DataManagerGUI import DataManagerGUI
from createdata import CSVEditorApp
from RepData import DataPlotter
from MLGUI import MLGUI
from First_Page import First_Page


class Controller:
    def __init__(self, root):
        self.dataManager = DataManager()
        self.root = root
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.first_page = First_Page(self.notebook, self)
        self.createdata_page = CSVEditorApp(self.notebook, self)
        self.ml_gui_page = MLGUI(self.notebook, self,self.dataManager)
        self.data_visualization_page = DataPlotter(self.notebook, self)
        self.data_management_page = DataManagerGUI(self.notebook, self, self.dataManager)
        self.notebook.add(self.first_page, text='First Page')
        self.notebook.add(self.createdata_page, text='Create Data')
        self.notebook.add(self.ml_gui_page, text='ML GUI')
        self.notebook.add(self.data_visualization_page, text='Data Visualization')
        self.notebook.add(self.data_management_page, text='Data Management')

        self.show_first_page()

    def show_first_page(self):
        self.notebook.select(0)  # Index of the First Page tab

    def show_create_data(self):
        self.notebook.select(1)  # Index of the Create Data tab

    def show_import_data(self):
        # Replace this with the correct index of the tab you want to show
        # For example, if Create Data is at index 1, replace it with 1
        self.notebook.select(1)

    def show_ml_gui(self):
        self.notebook.select(2)  # Index of the ML GUI tab

    def show_data_visualization(self):
        self.notebook.select(3)  # Index of the Data Visualization tab

    def show_manage_data(self):
        self.notebook.select(4)
    def update_dependents(self):
        print("update dependants")
        self.ml_gui_page.refresh()
        self.data_management_page.refresh()
