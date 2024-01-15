import os
import re

import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkintertable import TableCanvas

from DataManager import DataManager



class DataManagerGUI(tk.Frame):
    def __init__(self, root, controller,dataManager):
        super().__init__(root, bg="lightblue")
        self.deleted_columns= []
        # Create and place a frame for the dropdown
        self.dropdown_frame = ttk.Frame(self, padding=(10, 10, 10, 10))
        self.dropdown_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Create a frame to contain the checkboxes
        self.manage_frame = ttk.Frame(self)
        self.manage_frame.grid(row=1, column=0, columnspan=3, sticky="ew")

        # Configure row and column weights
        self.grid_rowconfigure(2, weight=1)  # Adjust the row weight as needed
        self.grid_columnconfigure(0, weight=1)  # Adjust the column weight as needed

        # Create Table Frame
        self.table_frame = ttk.Frame(self)
        self.table_frame.grid(row=3, column=0,columnspan=3, sticky="nsew")

        self.dataManager = dataManager
        self.controller = controller
        self.columns = None
        self.table=None
        self.create_dropdown_files()


        # Add buttons for managing data
        #self.create_data_management_buttons()



    def create_dropdown_files(self):


        # Create and place a dropdown for file choice
        self.dropdown_file_var = tk.StringVar()
        self.dropdown_file = ttk.Combobox(self.dropdown_frame, textvariable=self.dropdown_file_var, values=self.dataManager.csv_files)
        self.dropdown_file.pack(side="left", padx=(0, 10))

        # Set default value for dropdown
        if self.dataManager.csv_files:
            self.dropdown_file.set(self.dataManager.csv_files[0])

        # Add button to load selected CSV
        load_button = tk.Button(self.dropdown_frame, text="Load CSV", command=self.load_selected_csv)
        load_button.pack(side="left")

    def load_selected_csv(self):
        selected_file = self.dropdown_file_var.get()
        if selected_file:
            self.dataManager.load_data(selected_file)
            self.columns=self.dataManager.getColumns()
            self.create_data_management_buttons()
            self.create_table()

    def fix_invalid_columns(self):
        self.columns=self.dataManager.getColumns()

        # Remove characters that could cause problems in column names
        valid_column_name = lambda s: re.sub(r'[^a-zA-Z0-9_]', '', s)
        self.headers = [valid_column_name(col) for col in self.columns]

    def create_table(self):
        # Create a ttk.Treeview widget
        self.fix_invalid_columns()
        self.table = ttk.Treeview(self.table_frame, columns=self.headers, show="headings", selectmode="browse")

        # Add columns to the treeview
        for col in self.headers:
            self.table.heading(col, text=col)
            self.table.column(col, width=100, anchor=tk.CENTER)  # Adjust the width as needed

        # Insert data into the treeview
        for row in self.dataManager.data.to_numpy():
            self.table.insert("", "end", values=tuple(row))

        # Add a vertical scrollbar to the treeview
        y_scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=y_scrollbar.set)
        # Add a horizontal scrollbar to the treeview
        x_scrollbar = ttk.Scrollbar(self.table_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscroll=x_scrollbar.set)

        # Use pack for the treeview and scrollbar
        self.table.pack(side="left", fill="both", expand=True)
        y_scrollbar.pack(side="right", fill="y")
        x_scrollbar.pack(side="bottom", fill="x")  # Pack the horizontal scrollbar at the bottom

        # Bind a function to handle treeview item selection
        #self.table.bind("<ButtonRelease-1>", self.on_table_item_selected)
    def create_checkBox(self,callback):
        # Create a checkbox for each column
        frame= tk.Frame(self.manage_frame)
        frame.grid(row=0,column=1)
        for col in self.columns:
            var = tk.IntVar()
            checkbox = ttk.Checkbutton(frame, text=col, variable=var,
                                       command=lambda c=col: callback(c))
            checkbox.pack(side="left")

    def create_data_management_buttons(self):
        deleteLabel = tk.Label(self.manage_frame, text="Delete: ")
        deleteLabel.grid(row=0,column=0)
        self.create_checkBox(self.deleteColumn)

        # Roll back delete button
        rollBackDeleteBtn = tk.Button(self.manage_frame, text="Roll Back Delete", command=self.rollBackDelete)
        rollBackDeleteBtn.grid(row=0,column=3)

        # Handling missing values radio buttons
        missing_values_var = tk.StringVar(value="mean")  # Default option: fill missing values with mean
        missing_values_label = tk.Label(self.manage_frame, text="Handle Missing Values:")
        missing_values_label.grid(row=1,column=0)

        # Radio button to fill missing values with mean
        mean_radio = tk.Radiobutton(self.manage_frame, text="Fill with Mean", variable=missing_values_var,
                                    value="mean")
        mean_radio.grid(row=1,column=1)

        # Radio button to fill missing values with median
        median_radio = tk.Radiobutton(self.manage_frame, text="Fill with Median", variable=missing_values_var,
                                      value="median")
        median_radio.grid(row=1,column=2)

        # Radio button to drop rows with missing values
        drop_radio = tk.Radiobutton(self.manage_frame, text="Most frequent",
                                    variable=missing_values_var, value="most_frequent")
        drop_radio.grid(row=1,column=3)

        # Radio button to drop columns with missing values
        drop_column_radio = tk.Radiobutton(self.manage_frame, text="Drop Columns with Missing Values",
                                           variable=missing_values_var, value="drop_columns")
        drop_column_radio.grid(row=1,column=4)

        # Apply missing values handling when the radio button is selected
        def handle_missing_values():
            strategy = missing_values_var.get()  # Convert option to match method parameter
            self.dataManager.handle_missing_values(strategy)
            # Update the table or perform any necessary actions after handling missing values
            self.refresh_table()


        # Button to apply missing values handling
        handle_missing_values_btn = tk.Button(self.manage_frame, text="Apply", command=handle_missing_values)
        handle_missing_values_btn.grid(row=1, column=5)
        def to_numeric():
            self.dataManager.create_dummy_variables()

            self.refresh_table()

        # Button to change categorical to numeric
        change_categorical_btn = tk.Button(self.manage_frame, text="Change Categorical to Numeric",
                                           command=to_numeric)
        change_categorical_btn.grid(row=2, column=0)
        def save():
            self.dataManager.update_file(self.dataManager.data)
            self.controller.update_dependents()
        save_changes_btn= tk.Button(self.manage_frame, text="Save Changes", command=save)
        save_changes_btn.grid(row=3, column=3)

    def refresh_table(self):
        # Destroy all children of the table_frame
        for child in self.table_frame.winfo_children():
            child.destroy()
        for child in self.manage_frame.winfo_children():
            child.destroy()

        self.create_data_management_buttons()
        self.create_table()


    def deleteColumn(self,column):
        self.deleted_columns.append(column)
        print("deleted columns" , self.deleted_columns)
        self.dataManager.drop_columns(column)
        self.columns=self.dataManager.getColumns()
        print(self.columns)
        self.refresh_table()

    def rollBackDelete(self):
        if self.deleted_columns != []:

            last_deleted= self.deleted_columns.pop()
            print(last_deleted)
            self.dataManager.rollBackDelete(last_deleted)
            self.columns=self.dataManager.getColumns()
            self.refresh_table()

    def refresh(self):
        for child in self.table_frame.winfo_children():
            child.destroy()
        for child in self.manage_frame.winfo_children():
            child.destroy()
        for child in self.dropdown_frame.winfo_children():
            child.destroy()
        self.create_dropdown_files()



# Example usage:

