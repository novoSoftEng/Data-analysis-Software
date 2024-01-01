import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd
from tksheet import Sheet

def create_csv():
    file_name = file_name_var.get()
    if not file_name:
        messagebox.showerror("Erreur", "Veuillez entrer un nom de fichier.")
        return

    data = sheet.get_sheet_data()
    if not columns:
        messagebox.showerror("Erreur", "Veuillez définir au moins une colonne.")
        return

    df = pd.DataFrame(data[1:], columns=columns)
    df.to_csv(f'{file_name}.csv', index=False)
    messagebox.showinfo("Succès", f"Le fichier {file_name}.csv a été créé avec succès!")

def define_columns():
    global columns  # Utilisez la variable globale pour éviter la création d'une nouvelle liste
    num_columns = num_columns_var.get()
    try:
        num_columns = int(num_columns)
        if num_columns <= 0:
            raise ValueError("Le nombre de colonnes doit être un entier positif.")
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))
        return

    column_names = simpledialog.askstring("Noms des colonnes", "Entrez les noms des colonnes séparés par des virgules:")
    if not column_names:
        messagebox.showerror("Erreur", "Les noms de colonnes ne peuvent pas être vides.")
        return

    columns = column_names.split(',')
    sheet.headers(columns)
    num_columns_entry.config(state='normal')
    define_columns_button.config(state='normal')
    refresh_table()

def add_row():
    values = sheet.get_sheet_data()[0]
    sheet.insert_row(values)

def edit_column(col):
    new_name = simpledialog.askstring("Modifier le nom de colonne", f"Entrez le nouveau nom pour la colonne {col}:")
    if new_name:
        columns[columns.index(col)] = new_name
        refresh_table()

def refresh_table():
    sheet.headers(columns)
    data = sheet.get_sheet_data()
    sheet.set_sheet_data([[None] * len(columns)] + data[1:])

def on_cell_edit(event):
    row, col, value = event[0], event[1], event[2]
    print(f"Cellule éditée : Ligne {row}, Colonne {col}, Nouvelle valeur : {value}")

# Fenêtre principale
window = tk.Tk()
window.geometry('800x600')
window.title('Modification de Table')

file_name_var = tk.StringVar()
columns = []

tk.Label(window, text="Nom du fichier CSV (sans extension):").pack()
tk.Entry(window, textvariable=file_name_var).pack()

tk.Label(window, text="Nombre de colonnes:").pack()
num_columns_var = tk.StringVar()
num_columns_entry = tk.Entry(window, textvariable=num_columns_var)
num_columns_entry.pack()

define_columns_button = tk.Button(window, text="Définir les colonnes", command=define_columns)
define_columns_button.pack()

# tksheet
sheet = Sheet(window, page_up_down_select_row=True, edit_cell_validation=True)  # Activation de l'édition de cellules
sheet.enable_bindings("all")

sheet.enable_bindings(("single_select","row_select","column_width_resize","arrowkeys",

                        "right_click_popup_menu",

                        "rc_select",

                        "rc_insert_row",

                        "rc_delete_row",

                        "copy",

                        "cut",

                        "paste",

                        "delete",

                        "undo",

                        "edit_cell",

                        "end_edit_cell"))

sheet.extra_bindings("end_edit_cell")

sheet.pack(fill="both", expand=True)
sheet.set_options(edit_cell_validation=True)
add_row_button = tk.Button(window, text="Ajouter une ligne", command=add_row)
add_row_button.pack()

for col in columns:
    edit_col_button = tk.Button(window, text=f"Modifier {col}", command=lambda c=col: edit_column(c))
    edit_col_button.pack()

csv_button = tk.Button(window, text="Créer le fichier CSV", command=create_csv)
csv_button.pack()

sheet.extra_bindings([("<<TableEdited>>", on_cell_edit)])

window.mainloop()
