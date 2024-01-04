import tkinter as tk
from tkinter import filedialog
import shutil
import os
import pandas as pd

class DataImporter:
    def __init__(self, master):
        self.master = master
        self.master.title("Exemple de téléchargement et d'enregistrement de fichier")

        # Create and configure the frame
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(padx=10, pady=10)

        # Create widgets
        self.upload_button = tk.Button(self.frame, text="Télécharger le fichier", command=self.upload_file)
        self.status_label = tk.Label(self.frame, text="Aucun fichier sélectionné", wraplength=300)

        # Place widgets in the frame
        self.upload_button.pack(pady=10)
        self.status_label.pack()
        self.data=None

    def upload_file(self):
        file_path = filedialog.askopenfilename(title="Sélectionner un fichier", filetypes=[("Tous les fichiers", "*.*")])
        if file_path:
            try:
                # Get the current directory
                current_directory = os.getcwd()

                # Extract the file name
                file_name = os.path.basename(file_path)

                # Destination path in the current directory
                destination_path = os.path.join(current_directory, file_name)

                # Copy the file to the destination path
                shutil.copyfile(file_path, destination_path)
                self.data=pd.read_csv(file_name)

                self.status_label.config(text=f"Fichier '{file_name}' enregistré dans le répertoire courant")
            except Exception as e:
                self.status_label.config(text=f"Erreur lors de l'enregistrement du fichier : {str(e)}")
        else:
            self.status_label.config(text="Aucun fichier sélectionné")


root = tk.Tk()
data_importer = DataImporter(root)
root.mainloop()
