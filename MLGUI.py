import tkinter as tk
from tkinter import ttk

class MLGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI")

        # Create a StringVar to store the text input
        self.text_var = tk.StringVar()

        # Create and place a text input
        self.text_entry = tk.Entry(root, textvariable=self.text_var, width=30)
        self.text_entry.grid(row=0, column=0, padx=10, pady=10)

        # Create and place a dropdown
        self.dropdown_var = tk.StringVar()
        self.dropdown = ttk.Combobox(root, textvariable=self.dropdown_var, values=["Option 1", "Option 2", "Option 3"])
        self.dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Create and place a button
        self.evaluate_button = tk.Button(root, text="Evaluate", command=self.evaluate)
        self.evaluate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def evaluate(self):
        # Retrieve the entered text and selected dropdown value
        entered_text = self.text_var.get()
        selected_option = self.dropdown_var.get()

        # Do something with the data (for now, just print it)
        print("Entered Text:", entered_text)
        print("Selected Option:", selected_option)
    # Create the main Tkinter window
root = tk.Tk()

    # Create an instance of the SimpleGUI class
app = MLGUI(root)

    # Start the Tkinter event loop
root.mainloop()
