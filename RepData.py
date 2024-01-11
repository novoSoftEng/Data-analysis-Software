import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataPlotter(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()
        self.update_combobox_values(self.csv_file_combo)

    def create_widgets(self):
        self.create_combobox("CSV File", self.on_csv_selected)
        self.create_combobox("Column", None)
        self.create_combobox("Graph Type", None)

        self.plot_button = ttk.Button(self, text="Plot Graph", command=self.on_plot_button_click)
        self.plot_button.pack(pady=10)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def create_combobox(self, label, event_handler):
        ttk.Label(self, text=f"{label}:").pack()
        combo = ttk.Combobox(self, state="readonly")
        combo.pack(pady=5)
        if event_handler:
            combo.bind('<<ComboboxSelected>>', event_handler)

        if label == "Graph Type":
            combo['values'] = ['Line Plot', 'Scatter Plot', 'Histogram', 'Bar Plot']

        setattr(self, f"{label.lower().replace(' ', '_')}_combo", combo)

    def update_combobox_values(self,combo):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        files = [file for file in os.listdir(current_folder) if file.endswith('csv')]
        combo['values'] = files

    def load_csv_columns(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
        return header

    def on_csv_selected(self, event):
        selected_file = self.csv_file_combo.get()
        if selected_file:
            columns = self.load_csv_columns(selected_file)
            self.column_combo['values'] = columns
            self.column_combo.current(0)  # Select the first column by default

    def plot_graph(self, graph_type, data, xlabel, ylabel, title):
        self.ax.clear()
        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)

        if graph_type == 'Line Plot':
            self.ax.plot(data)
        elif graph_type == 'Scatter Plot':
            self.ax.scatter(range(len(data)), data)
        elif graph_type == 'Histogram':
            self.ax.hist(data, bins=10, color='green', edgecolor='black')
        elif graph_type == 'Bar Plot':
            self.ax.bar(range(len(data)), data, color='purple')

        self.canvas.draw()

    def on_plot_button_click(self):
        selected_file = self.csv_file_combo.get()
        selected_column = self.column_combo.get()

        if selected_file and selected_column:
            with open(selected_file, 'r') as file:
                reader = csv.DictReader(file)
                data = [float(row[selected_column]) for row in reader]

            graph_type = self.graph_type_combo.get()
            self.plot_graph(graph_type, data, 'Index', selected_column, f'{graph_type} of {selected_column}')

if __name__ == "__main__":
    root = tk.Tk()
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)
    app = DataPlotter(notebook, None)
    #notebook.add(app, text='Data Plotter')
    root.protocol("WM_DELETE_WINDOW", app.on_closing(root))  # handle the window close event
    root.mainloop()

def on_closing(root):
    root.destroy()
    sys.exit()


