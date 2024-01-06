import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataPlotter:
    def __init__(self, root,controller):
        self.root = root
        self.root.title("CSV Data Plotter")
        self.controller = controller
        self.create_widgets()
        self.update_combobox_values()

    def create_widgets(self):
        self.combo = ttk.Combobox(self.root, state="readonly")
        self.combo.pack(pady=10)

        self.column_combo = ttk.Combobox(self.root, state="readonly")
        self.column_combo.pack(pady=10)

        self.graph_type_combo = ttk.Combobox(self.root, values=['Line Plot', 'Scatter Plot', 'Histogram', 'Bar Plot'], state="readonly")
        self.graph_type_combo.pack(pady=10)

        self.plot_button = ttk.Button(self.root, text="Plot Graph", command=self.on_plot_button_click)
        self.plot_button.pack(pady=10)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.combo.bind('<<ComboboxSelected>>', self.on_csv_selected)

    def update_combobox_values(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        csv_files = [file for file in os.listdir(current_folder) if file.endswith('.csv')]
        self.combo['values'] = csv_files

    def load_csv_columns(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
        return header

    def on_csv_selected(self, event):
        selected_file = self.combo.get()
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
        selected_file = self.combo.get()
        selected_column = self.column_combo.get()

        if selected_file and selected_column:
            with open(selected_file, 'r') as file:
                reader = csv.DictReader(file)
                data = [float(row[selected_column]) for row in reader]

            graph_type = self.graph_type_combo.get()
            self.plot_graph(graph_type, data, 'Index', selected_column, f'{graph_type} of {selected_column}')

    def on_closing(self):
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataPlotter(root)
    root.mainloop()
