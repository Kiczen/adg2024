import os
import numpy as np

path = os.path.join(os.path.expanduser("~"), "Desktop", "Wszystko", "Lekcje", "sem5", "Algorytmy danych geoprzestrzennych", "2024.12.06")
os.chdir(path)


def stat(obiekty, geom_type):
    wartosci = []
    for obiekt in obiekty:
        geom = obiekt.geometry()
        if geom is not None:
            if geom_type == "powierzchnia" and geom.type() == 2:
                wartosci.append(geom.area())
            elif geom_type == "długość" and geom.type() == 1:
                wartosci.append(geom.length())
    if wartosci:
        minimum = np.min(wartosci)
        maksimum = np.max(wartosci)
        srednia = np.mean(wartosci)
        odchylenie = np.std(wartosci)
        liczba_wartosci = len(wartosci)
        return f"min: {minimum}, max: {maksimum}, srednia: {srednia}, odchylenie: {odchylenie}, liczba: {liczba_wartosci}"
    else:
        return "Brak danych"


powiaty = "powiaty.gpkg"
warstwa = QgsVectorLayer(powiaty, "wektor", "ogr")
obiekty = warstwa.getFeatures()


statystyki_powierzchni = stat(obiekty, "powierzchnia")
print(statystyki_powierzchni)

statystyki_dlugosci = stat(obiekty, "długość")
print(statystyki_dlugosci)
