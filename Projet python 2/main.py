import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from analysis import calculate_statistics
from report_generation import PDF
from visualization import PerformanceVisualizer

class PerformanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application de Rapport de Performance")
        self.geometry("400x300")
        self.file_path = "performance_data.csv"
        self.data = None
        self.performance_summary = None

        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Entrer les données de performance")
        label.pack(pady=10)

        frame = ttk.Frame(self)
        frame.pack(pady=10)

        ttk.Label(frame, text="Nom:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Tâches Accomplies:").grid(row=1, column=0, padx=5, pady=5)
        self.tasks_entry = ttk.Entry(frame)
        self.tasks_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Heures Travaillées:").grid(row=2, column=0, padx=5, pady=5)
        self.hours_entry = ttk.Entry(frame)
        self.hours_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Ajouter des données", command=self.add_data).grid(row=3, columnspan=2, padx=5, pady=10)

        ttk.Button(self, text="Générer le rapport", command=self.generate_report).pack(pady=10)

    def add_data(self):
        name = self.name_entry.get()
        tasks_completed = self.tasks_entry.get()
        hours_worked = self.hours_entry.get()

        if not name or not tasks_completed or not hours_worked:
            messagebox.showerror("Erreur", "Veuillez entrer tous les champs.")
            return

        try:
            tasks_completed = int(tasks_completed)
            hours_worked = float(hours_worked)
        except ValueError:
            messagebox.showerror("Erreur", "Entrée invalide pour les tâches accomplies ou les heures travaillées.")
            return

        new_data = pd.DataFrame({
            "Nom": [name],
            "Tâches_Accomplies": [tasks_completed],
            "Heures_Travaillées": [hours_worked]
        })

        if self.data is None:
            self.data = new_data
        else:
            self.data = pd.concat([self.data, new_data], ignore_index=True)

        messagebox.showinfo("Succès", "Données ajoutées avec succès.")

        self.name_entry.delete(0, tk.END)
        self.tasks_entry.delete(0, tk.END)
        self.hours_entry.delete(0, tk.END)

    def generate_report(self):
        if self.data is None or self.data.empty:
            messagebox.showerror("Erreur", "Aucune donnée disponible pour générer le rapport.")
            return

        self.performance_summary = calculate_statistics(self.data)

        pdf = PDF()
        pdf.add_page()
        pdf.chapter_title('Résumé des Performances')
        pdf.chapter_body(self.performance_summary.to_string())
        pdf.output('rapport_de_performance.pdf')

        messagebox.showinfo("Succès", "Rapport généré avec succès.")

        # Visualisation avec Panda3D
        visualizer = PerformanceVisualizer(self.performance_summary)
        visualizer.start_visualizer()

if __name__ == "__main__":
    app = PerformanceApp()
    app.mainloop()