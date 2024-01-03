import tkinter as tk
from tkinter import ttk
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier, SGDClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris

from ConfusionMatrixDisplay import ConfusionMatrixDisplay
from ML import ML
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Table import Table

# Load the Iris dataset
iris = load_iris()

# Access the features and target variables
X = iris.data  # Features
y = iris.target  # Target





class MLGUI:
    def __init__(self, root):
        root.geometry("800x600")
        self.root = root
        self.root.title("ML Model Evaluator")

        # Initialize an empty label to display the confusion matrix
        self.matrix_label = tk.Label(root, text="", font=("Helvetica", 10))
        self.matrix_label.grid(row=0, column=5, padx=10, pady=10, columnspan=2)

        # Create and place a dropdown
        self.dropdown_var = tk.StringVar()
        models = ["Logistic Regression", "RandomForestClassifier", "Ridge Classifier", "SGD Classifier",
                  "Support Vector Machine"]
        self.dropdown = ttk.Combobox(root, textvariable=self.dropdown_var, values=models)
        self.dropdown.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Set default value for dropdown
        self.dropdown.set(models[0])

        # Create and place a button
        self.evaluate_button = tk.Button(root, text="Evaluate", command=self.evaluate)
        self.evaluate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def create_confusion_matrix(self,cm):
        self.cm_display = ConfusionMatrixDisplay(root, cm, row=1, column=3)


    def evaluate(self):
        selected_model = self.dropdown_var.get()
        model = None

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
        ml = ML(model, X, y)

        # Evaluate the model
        accuracy, confusion_matrix = ml.evaluate()
        self.create_confusion_matrix(confusion_matrix)
        # Print the results
        print(f"Accuracy: {accuracy}")
        print("Confusion Matrix:")
        print(confusion_matrix)

root = tk.Tk()

# Create an instance of the MLGUI class
app = MLGUI(root)

    # Start the Tkinter event loop
root.mainloop()

