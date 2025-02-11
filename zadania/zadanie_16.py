import os
import math
import csv


path = os.path.join(os.path.expanduser("~"), "Desktop", "Wszystko", "Lekcje", "sem5", "Algorytmy danych geoprzestrzennych", "2025.01.17")
os.chdir(path)

profil = "profil.csv"

def surface_distance(plik):
    punkty = []
    with open(profil, newline='', encoding='utf-8') as plik:
        r = csv.reader(plik)
        next(r)
        for row in r:
            x, y, z = map(float, row[1:])
            punkty.append((x, y, z))
    dist = 0
    for i in range(len(punkty) - 1):
        x1, y1, z1 = punkty[i]
        x2, y2, z2 = punkty[i + 1]
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return round(dist, 2)

surface_distance(profil)

