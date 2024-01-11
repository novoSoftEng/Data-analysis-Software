import os
import tkinter as tk
from tkinter import ttk

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier, SGDClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris

from ConfusionMatrixDisplay import ConfusionMatrixDisplay
from DataManager import DataManager
from ML import ML










class MLGUI(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="lightblue")
        self.dropdown_var = None
        self.csv_files=[]
        self.find_data_files()
        self.controller = controller
        self.X=None
        self.y=None

        self.create_dropdown_model()
        self.create_dropdown_files()
        self.create_dropdown_target()
        self.create_radio_buttons_prepr()

        


    def create_dropdown_files(self):
        # Create and place a frame for the dropdown
        dropdown_frame = ttk.Frame(self, padding=(10, 10, 10, 10))
        dropdown_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Create and place a dropdown for file choice
        self.dropdown_file_var = tk.StringVar()
        self.dropdown_file = ttk.Combobox(dropdown_frame, textvariable=self.dropdown_file_var, values=self.csv_files)
        self.dropdown_file.pack(side="left", padx=(0, 10))

        # Set default value for dropdown
        self.dropdown_file.set(self.csv_files[0])
    def create_dropdown_target(self):
        # Create and place a frame for the dropdown
        dropdown_frame = ttk.Frame(self, padding=(10, 10, 10, 10))
        dropdown_frame.grid(row=0, column=4, columnspan=2, sticky="ew")

        # Create and place a dropdown for file choice
        self.dropdown_target_var = tk.StringVar()
        # making data frame
        data = pd.read_csv(self.dropdown_file_var.get())
        columns=[col for col in data.columns]
        self.dropdown_target = ttk.Combobox(dropdown_frame, textvariable=self.dropdown_target_var, values=columns)
        self.dropdown_target.pack(side="left", padx=(0, 10))

        # Set default value for dropdown
        self.dropdown_target.set(columns[-1])

    def create_dropdown_model(self):
        # Create and place a frame for the dropdown
        dropdown_frame = ttk.Frame(self, padding=(10, 10, 10, 10))
        dropdown_frame.grid(row=0, column=2, columnspan=2, sticky="ew")

        # Create and place a dropdown for model choice
        self.dropdown_model_var = tk.StringVar()
        models = ["Logistic Regression", "RandomForestClassifier", "Ridge Classifier", "SGD Classifier",
                  "Support Vector Machine"]
        self.dropdown_model = ttk.Combobox(dropdown_frame, textvariable=self.dropdown_model_var, values=models)
        self.dropdown_model.pack(side="left", padx=(0, 10))

        # Set default value for dropdown
        self.dropdown_model.set(models[0])

    def create_radio_buttons_prepr(self):
        # Create and place a frame for radio buttons
        radio_frame = ttk.Frame(self, padding=(10, 10, 10, 10))
        radio_frame.grid(row=1, column=0, columnspan=4, sticky="w")

        # Create a StringVar to store the selected value
        self.selected_prep = tk.StringVar()

        # Create a label with the text "Preprocessing"
        preprocessing_label = tk.Label(radio_frame, text="Preprocessing : ", font=("Helvetica", 12))
        preprocessing_label.grid(row=0, column=0, padx=(0, 10), sticky="w")

        # Create and place radio buttons
        self.radio_button1 = ttk.Radiobutton(radio_frame, text="None", variable=self.selected_prep, value=None)
        self.radio_button1.grid(row=0, column=1, padx=(0, 10))

        self.radio_button2 = ttk.Radiobutton(radio_frame, text="Standardization", variable=self.selected_prep,
                                             value="stand")
        self.radio_button2.grid(row=0, column=2, padx=(0, 10))

        self.radio_button3 = ttk.Radiobutton(radio_frame, text="Normalization", variable=self.selected_prep,
                                             value="norm")
        self.radio_button3.grid(row=0, column=3, padx=(0, 10))

        # Create and place a button
        self.evaluate_button = tk.Button(self, text="Evaluate", command=self.evaluate)
        self.evaluate_button.grid(row=2, column=0, columnspan=4, pady=10)

    def create_confusion_matrix(self,cm):
        self.cm_display = ConfusionMatrixDisplay(self, cm, row=0, column=4)


    def evaluate(self):
        selected_model = self.dropdown_model_var.get()
        selected_file = self.dropdown_file_var.get()
        data=pd.read_csv(selected_file)
        selected_target= self.dropdown_target_var.get()
        self.X = data.drop([selected_target],axis=1)
        self.y = data[selected_target]

        # Map models to corresponding classes
        model_classes = {
            "Logistic Regression": LogisticRegression(),
            "RandomForestClassifier": RandomForestClassifier(n_estimators=100),
            "Ridge Classifier": RidgeClassifier(),
            "SGD Classifier": SGDClassifier(),
            "Support Vector Machine": SVC()
        }

        # Get the selected model class
        model = model_classes.get(selected_model)

        # Do something with the data (for now, just print it)
        print("Selected Option:", selected_model)
        print("Model:", model)
        norm=False
        stand=False
        if self.selected_prep == "norm":
            norm=True
        elif self.selected_prep == "stand":
            stand=True
        ml = ML(model, self.X, self.y,stand=stand,norm=norm)

        # Evaluate the model
        accuracy, confusion_matrix = ml.evaluate()
        self.create_confusion_matrix(confusion_matrix)

    def find_data_files(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        self.csv_files = [file for file in os.listdir(current_folder) if file.endswith('.csv')]
