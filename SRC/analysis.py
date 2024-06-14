import pandas as pd

def calculate_statistics(data):
    data['Productivité'] = data['Tâches_Accomplies'] / data['Heures_Travaillées']
    return data