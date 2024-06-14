# performance_report.py
class EmployeePerformance:
    # Définition de la classe EmployeePerformance
    pass
class PerformanceReport:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.performance_summary = None

    def load_data(self):
        try:
            self.data = load_data(self.file_path)
            if self.data is not None:
                self.data = preprocess_data(self.data)
            else:
                messagebox.showerror("Error", "Failed to load data.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")

    def generate_report(self):
        if self.data is None:
            messagebox.showerror("Error", "No data loaded. Please load data first.")
            return
        
        try:
            self.performance_summary = calculate_statistics(self.data)
            pdf_generator = PDF()
            pdf_generator.add_page()
            pdf_generator.chapter_title('Résumé des Performances')
            pdf_generator.chapter_body(self.performance_summary.to_string())
            pdf_generator.output('rapport_performance.pdf')
            messagebox.showinfo("Success", "Report generated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate report: {str(e)}")
