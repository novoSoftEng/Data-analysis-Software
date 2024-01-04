import tkinter as tk
from tkinter import ttk
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier, SGDClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris

from ConfusionMatrixDisplay import ConfusionMatrixDisplay
from ML import ML




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

        # Create and place a frame for the dropdown
        dropdown_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
        dropdown_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Create and place a dropdown
        self.dropdown_var = tk.StringVar()
        models = ["Logistic Regression", "RandomForestClassifier", "Ridge Classifier", "SGD Classifier",
                  "Support Vector Machine"]
        self.dropdown = ttk.Combobox(dropdown_frame, textvariable=self.dropdown_var, values=models)
        self.dropdown.pack(side="left", padx=(0, 10))

        # Set default value for dropdown
        self.dropdown.set(models[0])

        # Create and place a frame for radio buttons
        radio_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
        radio_frame.grid(row=1, column=0, columnspan=4, sticky="w")

        # Create a StringVar to store the selected value
        self.selected_prep = tk.StringVar()

        # Create and place radio buttons
        self.radio_button1 = ttk.Radiobutton(radio_frame, text="None", variable=self.selected_prep, value=None)
        self.radio_button1.pack(side="left", padx=(0, 10))

        self.radio_button2 = ttk.Radiobutton(radio_frame, text="Standardization", variable=self.selected_prep,
                                             value="stand")
        self.radio_button2.pack(side="left", padx=(0, 10))

        self.radio_button3 = ttk.Radiobutton(radio_frame, text="Normalization", variable=self.selected_prep,
                                             value="norm")
        self.radio_button3.pack(side="left", padx=(0, 10))

        # Create and place a button
        self.evaluate_button = tk.Button(root, text="Evaluate", command=self.evaluate)
        self.evaluate_button.grid(row=2, column=0, columnspan=4, pady=10)

    def create_confusion_matrix(self,cm):
        self.cm_display = ConfusionMatrixDisplay(root, cm, row=0, column=4)


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
        norm=False
        stand=False
        if self.selected_prep == "norm":
            norm=True
        elif self.selected_prep == "stand":
            stand=True
        ml = ML(model, X, y,stand=stand,norm=norm)

        # Evaluate the model
        accuracy, confusion_matrix = ml.evaluate()
        self.create_confusion_matrix(confusion_matrix)

root = tk.Tk()

# Create an instance of the MLGUI class
app = MLGUI(root)

    # Start the Tkinter event loop
root.mainloop()

