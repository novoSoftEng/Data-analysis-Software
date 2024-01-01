import tkinter as tk
from tkinter import ttk, simpledialog
import pandas as pd
from openpyxl import Workbook

# Function to create a CSV file
def create_csv(data, columns, file_name):
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(f'{file_name}.csv', index=False)
    tk.messagebox.showinfo("Succès", f"Le fichier {file_name}.csv a été créé avec succès!")
# Function to open a form for data input
def open_data_form():
    form = tk.Toplevel(window)

    # Create an entry for each column
    entries = {}
    for col in columns:
        tk.Label(form, text=f"{col}:").pack()
        entries[col] = tk.Entry(form)
        entries[col].pack()

    # Function to handle form submission
    def submit_form():
        values = [entries[col].get() for col in columns]
        table.insert(parent='', index=0, values=values)
        form.destroy()

    # Submit button
    tk.Button(form, text="Submit", command=submit_form).pack()

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# Get the CSV file name from the user
file_name = simpledialog.askstring("Input", "Enter the CSV file name (without extension):")

# Get the number of columns from the user
num_columns = simpledialog.askinteger("Input", "Enter the number of columns:", initialvalue=3)

# Get column names from the user
columns = []
for i in range(num_columns):
    column_name = simpledialog.askstring("Input", f"Enter name for column {i + 1}:")
    columns.append(column_name)

# treeview
table = ttk.Treeview(window, columns=columns, show='headings')

for name in columns:
    table.heading(name, text=name)

table.pack(fill='both', expand=True)

# Create CSV file button
csv_button = tk.Button(window, text="Create CSV File", command=lambda: create_csv([table.item(item)['values'] for item in table.get_children()], columns, file_name))
csv_button.pack()

# Open data input form button
form_button = tk.Button(window, text="Open Data Input Form", command=open_data_form)
form_button.pack()

# events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    print('delete')
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# run
window.mainloop()
