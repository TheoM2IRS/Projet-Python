from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, LColor
import joblib
import numpy as np

class IDSVisualization(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Charger le modèle et le scaler
        self.model = joblib.load('rf_model.pkl')
        self.scaler = joblib.load('scaler.pkl')

        # Générer des données de test pour la visualisation
        self.generate_test_data()

    def generate_test_data(self):
        # Générer quelques données de test aléatoires
        np.random.seed(42)
        num_samples = 100
        data = np.random.rand(num_samples, len(column_names) - 1)
        data = self.scaler.transform(data)
        
        # Prédire les étiquettes
        predictions = self.model.predict(data)

        for i in range(num_samples):
            x, y, z = data[i, :3]  # Utiliser les trois premières caractéristiques pour la position
            color = LColor(1, 0, 0, 1) if predictions[i] else LColor(0, 1, 0, 1)
            self.create_point(Point3(x, y, z), color)

    def create_point(self, position, color):
        # Créer une géométrie simple pour le point
        point = self.loader.loadModel("models/box")
        point.setScale(0.1)
        point.setPos(position)
        point.setColor(color)
        point.reparentTo(self.render)

# Démarrer la visualisation
app = IDSVisualization()
app.run()
