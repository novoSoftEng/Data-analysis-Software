import tkinter as tk
from tkinter import filedialog
import shutil
import os


def upload_file():
    file_path = filedialog.askopenfilename(title="Sélectionner un fichier", filetypes=[("Tous les fichiers", "*.*")])
    if file_path:
        try:
            # Obtenir le répertoire courant
            current_directory = os.getcwd()

            # Extraire le nom du fichier
            file_name = os.path.basename(file_path)

            # Chemin de destination dans le répertoire courant
            destination_path = os.path.join(current_directory, file_name)

            # Copier le fichier vers le chemin de destination
            shutil.copyfile(file_path, destination_path)

            status_label.config(text=f"Fichier '{file_name}' enregistré dans le répertoire courant")
        except Exception as e:
            status_label.config(text=f"Erreur lors de l'enregistrement du fichier : {str(e)}")
    else:
        status_label.config(text="Aucun fichier sélectionné")


# Créer la fenêtre principale
window = tk.Tk()
window.title("Exemple de téléchargement et d'enregistrement de fichier")

# Créer et configurer le cadre
frame = tk.Frame(window, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Créer les widgets
upload_button = tk.Button(frame, text="Télécharger le fichier", command=upload_file)
status_label = tk.Label(frame, text="Aucun fichier sélectionné", wraplength=300)

# Placer les widgets dans le cadre
upload_button.pack(pady=10)
status_label.pack()

window.mainloop()
