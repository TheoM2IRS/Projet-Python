# gui.py

import tkinter as tk
from tkinter import messagebox
import pandas as pd
class PerformanceReportApp:
    # Définition de la classe
    pass

class PerformanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Saisie des Performances")

        # Liste pour stocker les entrées d'utilisateur
        self.user_entries = []

        # Créer un cadre de défilement pour les entrées utilisateurs
        self.scrollframe = tk.Frame(root)
        self.scrollframe.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.scrollframe)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.scrollframe, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Bouton pour ajouter un utilisateur
        tk.Button(root, text="Ajouter Utilisateur", command=self.ajouter_utilisateur).pack()

        self.file_path = 'performance_data.csv'

    def ajouter_utilisateur(self):
        # Créer un cadre pour chaque utilisateur avec les champs requis
        user_frame = tk.Frame(self.frame)
        user_frame.pack(pady=5)

        tk.Label(user_frame, text="Nom de l'employé :").grid(row=0, column=0)
        nom_entry = tk.Entry(user_frame)
        nom_entry.grid(row=0, column=1)

        tk.Label(user_frame, text="Tâches Accomplies :").grid(row=1, column=0)
        taches_entry = tk.Entry(user_frame)
        taches_entry.grid(row=1, column=1)

        tk.Label(user_frame, text="Heures Travaillées :").grid(row=2, column=0)
        heures_entry = tk.Entry(user_frame)
        heures_entry.grid(row=2, column=1)

        self.user_entries.append((nom_entry, taches_entry, heures_entry))

    def enregistrer_donnees(self):
        # Vérifier s'il y a des utilisateurs à enregistrer
        if not self.user_entries:
            messagebox.showwarning("Aucune Donnée", "Aucun utilisateur à enregistrer.")
            return

        # Préparer les données à enregistrer dans un DataFrame
        data = {
            'Nom': [],
            'Tâches_Accomplies': [],
            'Heures_Travaillées': []
        }

        for nom_entry, taches_entry, heures_entry in self.user_entries:
            nom = nom_entry.get()
            taches = taches_entry.get()
            heures = heures_entry.get()

            if nom and taches and heures:
                try:
                    taches = int(taches)
                    heures = int(heures)
                except ValueError:
                    messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques pour Tâches Accomplies et Heures Travaillées.")
                    return

                data['Nom'].append(nom)
                data['Tâches_Accomplies'].append(taches)
                data['Heures_Travaillées'].append(heures)
            else:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
                return

        # Ajouter les données au DataFrame et enregistrer dans le fichier CSV
        df = pd.DataFrame(data)
        try:
            existing_data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            existing_data = pd.DataFrame(columns=['Nom', 'Tâches_Accomplies', 'Heures_Travaillées'])

        updated_data = pd.concat([existing_data, df], ignore_index=True)
        updated_data.to_csv(self.file_path, index=False)

        messagebox.showinfo("Succès", "Données enregistrées avec succès.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PerformanceApp(root)

    tk.Button(root, text="Enregistrer Données", command=app.enregistrer_donnees).pack()

    root.mainloop()