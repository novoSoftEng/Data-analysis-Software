import tkinter as tk
from tkinter import ttk
import numpy as np

class ConfusionMatrixDisplay:
    def __init__(self, root, cm, row=0, column=1):
        self.root = root
        self.cm = cm

        # Create a Frame to contain the Canvas widget
        self.frame = ttk.Frame(root)
        self.frame.grid(row=row, column=column, padx=10, pady=10)

        # Create a Canvas widget to display the confusion matrix
        self.canvas = tk.Canvas(self.frame, width=300, height=300)
        self.canvas.pack()

        # Display the confusion matrix on the Canvas
        self.display_confusion_matrix()

    def display_confusion_matrix(self):
        rows, cols = self.cm.shape
        cell_width = 300 // cols
        cell_height = 300 // rows

        for i in range(rows):
            for j in range(cols):
                cell_value = self.cm[i, j]
                x0, y0 = j * cell_width, i * cell_height
                x1, y1 = (j + 1) * cell_width, (i + 1) * cell_height
                color = "blue" if i == j else "red"

                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(cell_value), fill="white")

