import pandas as pd

def load_data(file_path):
    # Charger les données
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

def preprocess_data(data):
    # Prétraitement des données
    # Ajoutez ici les étapes de nettoyage et de transformation nécessaires
    return data
