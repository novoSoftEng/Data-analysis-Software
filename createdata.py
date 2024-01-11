import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd
from tksheet import Sheet


class CSVEditorApp(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="lightblue")
        self.controller = controller

        self.file_name_var = tk.StringVar()
        self.columns = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Nom du fichier CSV (sans extension):").pack()
        tk.Entry(self, textvariable=self.file_name_var).pack()

        tk.Label(self, text="Nombre de colonnes:").pack()
        self.num_columns_var = tk.StringVar()
        self.num_columns_entry = tk.Entry(self, textvariable=self.num_columns_var)
        self.num_columns_entry.pack()

        self.define_columns_button = tk.Button(self, text="Définir les colonnes", command=self.define_columns)
        self.define_columns_button.pack()

        # tksheet
        self.sheet = Sheet(self, page_up_down_select_row=True, edit_cell_validation=True)
        self.setup_sheet_bindings()
        self.sheet.pack(fill="both", expand=True)

        self.add_row_button = tk.Button(self, text="Ajouter une ligne", command=self.add_row)
        self.add_row_button.pack()

        self.csv_button = tk.Button(self, text="Créer le fichier CSV", command=self.create_csv)
        self.csv_button.pack()

        self.sheet.extra_bindings([("<<TableEdited>>", self.on_cell_edit)])
        self.back_button = tk.Button(self, text="Retour à la première page", command=self.controller.show_first_page)
        self.back_button.pack()

    def setup_sheet_bindings(self):
        self.sheet.enable_bindings("all")
        self.sheet.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys",
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
        self.sheet.extra_bindings("end_edit_cell")
        self.sheet.set_options(edit_cell_validation=True)

    def create_csv(self):
        file_name = self.file_name_var.get()
        if not file_name:
            messagebox.showerror("Erreur", "Veuillez entrer un nom de fichier.")
            return

        data = self.sheet.get_sheet_data()
        if not data:
            messagebox.showerror("Erreur", "Aucune donnée à enregistrer.")
            return

        columns = data[0]  # La première ligne contient les noms de colonnes
        if not columns:
            messagebox.showerror("Erreur", "Veuillez définir au moins une colonne.")
            return

        df = pd.DataFrame(data[1:], columns=columns)
        df.to_csv(f'{file_name}.csv', index=False)
        messagebox.showinfo("Succès", f"Le fichier {file_name}.csv a été créé avec succès!")

    def define_columns(self):
        num_columns = self.num_columns_var.get()
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

        self.columns = column_names.split(',')
        self.sheet.headers(self.columns)
        self.num_columns_entry.config(state='normal')
        self.define_columns_button.config(state='normal')
        self.refresh_table()

    def add_row(self):
        num_columns = int(self.num_columns_var.get())
        empty_values = [""] * num_columns
        self.sheet.insert_row(empty_values)

    def refresh_table(self):
        self.sheet.headers(self.columns)
        data = self.sheet.get_sheet_data()
        self.sheet.set_sheet_data([[None] * len(self.columns)] + data[1:])

    def on_cell_edit(self, event):
        row, col, value = event[0], event[1], event[2]
        print(f"Cellule éditée : Ligne {row}, Colonne {col}, Nouvelle valeur : {value}")


if __name__ == "__main__":
    window = tk.Tk()
    app = CSVEditorApp(window, None)
    app.pack(fill="both", expand=True)
    window.mainloop()
