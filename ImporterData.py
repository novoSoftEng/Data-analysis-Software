import tkinter as tk
from tkinter import filedialog
import shutil
import os

class ImporterData:
    def __init__(self,controller):
        self.window = tk.Tk()
        self.window.title("Exemple de téléchargement et d'enregistrement de fichier")
        self.controller=controller
        # Create and configure the frame
        self.frame = tk.Frame(self.window, padx=20, pady=20)
        self.frame.pack(padx=10, pady=10)

        # Create the widgets
        self.upload_button = tk.Button(self.frame, text="Télécharger le fichier", command=self.upload_file)
        self.status_label = tk.Label(self.frame, text="Aucun fichier sélectionné", wraplength=300)

        # Place the widgets in the frame
        self.upload_button.pack(pady=10)
        self.status_label.pack()

    def upload_file(self):
        file_path = filedialog.askopenfilename(title="Sélectionner un fichier", filetypes=[("Tous les fichiers", "*.*")])
        if file_path:
            try:
                current_directory = os.getcwd()
                file_name = os.path.basename(file_path)
                destination_path = os.path.join(current_directory, file_name)
                shutil.copyfile(file_path, destination_path)

                self.status_label.config(text=f"Fichier '{file_name}' enregistré dans le répertoire courant")
                self.controller.update_dependents()
            except Exception as e:
                self.status_label.config(text=f"Erreur lors de l'enregistrement du fichier : {str(e)}")
        else:
            self.status_label.config(text="Aucun fichier sélectionné")

    def run(self):
        # Run the Tkinter main loop
        self.window.mainloop()




