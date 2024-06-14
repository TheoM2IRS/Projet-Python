from panda3d.core import TextNode
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
import pandas as pd

class PerformanceVisualizer(ShowBase):
    def __init__(self, performance_summary):
        ShowBase.__init__(self)
        self.title = OnscreenText(text="Rapport de Performance",
                                  parent=self.a2dTopLeft, scale=0.07,
                                  pos=(0.08, -0.1), fg=(1, 1, 1, 1),
                                  align=TextNode.ALeft)
        self.data = performance_summary

    def show_data(self):
        y = -0.2
        for index, row in self.data.iterrows():
            text = f"{row['Nom']}: Tâches Accomplies: {row['Tâches_Accomplies']}, Heures Travaillées: {row['Heures_Travaillées']}, Productivité: {row['Productivité']:.2f}"
            OnscreenText(text=text,
                         parent=self.a2dTopLeft, scale=0.05,
                         pos=(0.08, y), fg=(1, 1, 1, 1),
                         align=TextNode.ALeft)
            y -= 0.07

    def start_visualizer(self):
        if self.data is None or self.data.empty:
            print("Aucune donnée à visualiser.")
            return

        self.show_data()
        self.run()
