import tkinter as tk
from tkinter import simpledialog, messagebox
from tksheet import Sheet

# Fonction pour créer un fichier CSV
def create_csv():
    file_name = file_name_var.get()
    if not file_name:
        messagebox.showerror("Erreur", "Veuillez entrer un nom de fichier.")
        return

    data = sheet.get_sheet_data()
    if not columns:
        messagebox.showerror("Erreur", "Veuillez définir au moins une colonne.")
        return

    df = pd.DataFrame(data[1:], columns=columns)  # Skip the first row which contains column names
    df.to_csv(f'{file_name}.csv', index=False)
    # Afficher un message de succès
    messagebox.showinfo("Succès", f"Le fichier {file_name}.csv a été créé avec succès!")


# Fonction pour ajouter une ligne à la table
def add_row():
    values = sheet.get_sheet_data()[0]
    sheet.insert_row(values)


# Fonction pour éditer le nom de colonne
def edit_column(col):
    new_name = simpledialog.askstring("Modifier le nom de colonne", f"Entrez le nouveau nom pour la colonne {col}:")
    if new_name:
        columns[columns.index(col)] = new_name
        refresh_table()


# Fonction pour rafraîchir la table avec les nouvelles colonnes
def refresh_table():
    sheet.headers(columns)
    data = sheet.get_sheet_data()
    sheet.set_sheet_data([[None] * len(columns)] + data[1:])


# Fenêtre principale
window = tk.Tk()
window.geometry('800x600')
window.title('Modification de Table')

# Variables pour stocker le nom du fichier et les colonnes
file_name_var = tk.StringVar()
columns = []

# Entrée pour le nom du fichier
tk.Label(window, text="Nom du fichier CSV (sans extension):").pack()
tk.Entry(window, textvariable=file_name_var).pack()

# Entrée pour le nombre de colonnes
tk.Label(window, text="Nombre de colonnes:").pack()
num_columns_var = tk.StringVar()
num_columns_entry = tk.Entry(window, textvariable=num_columns_var)
num_columns_entry.pack()


# Bouton pour définir le nombre de colonnes et créer la table
def define_columns():
    num_columns = num_columns_var.get()
    try:
        num_columns = int(num_columns)
        if num_columns <= 0:
            raise ValueError("Le nombre de colonnes doit être un entier positif.")
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))
        return

    for i in range(num_columns):
        column_name = simpledialog.askstring("Nom de la colonne", f"Entrez le nom de la colonne {i + 1}:")
        if not column_name:
            messagebox.showerror("Erreur", "Le nom de la colonne ne peut pas être vide.")
            return
        columns.append(column_name)

    sheet.headers(columns)
    num_columns_entry.config(state='disabled')
    define_columns_button.config(state='disabled')
    refresh_table()


define_columns_button = tk.Button(window, text="Définir les colonnes", command=define_columns)
define_columns_button.pack()

# tksheet
sheet = Sheet(window, page_up_down_select_row=True)
sheet.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys", "right_click_popup_menu", "rc_select",
                       "rc_insert_column", "rc_delete_column", "rc_delete_row"))
sheet.pack(fill="both", expand=True)

# Bouton pour ajouter une ligne
add_row_button = tk.Button(window, text="Ajouter une ligne", command=add_row)
add_row_button.pack()

# Boutons pour éditer le nom de colonnes
for col in columns:
    edit_col_button = tk.Button(window, text=f"Modifier {col}", command=lambda c=col: edit_column(c))
    edit_col_button.pack()

# Bouton pour créer le fichier CSV
csv_button = tk.Button(window, text="Créer le fichier CSV", command=create_csv)
csv_button.pack()

# Événements
def item_select(_):
    print(sheet.get_selected_cells())

def delete_items(_):
    selected_rows = sheet.get_selected_rows()
    sheet.delete_row(selected_rows)

sheet.extra_bindings([("cell_select", item_select), ("<Delete>", delete_items)])

# Exécuter l'application
window.mainloop()
