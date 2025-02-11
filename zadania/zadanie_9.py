import os

path = os.path.join(os.path.expanduser("~"), "Desktop", "Wszystko", "Lekcje", "sem5", "Algorytmy danych geoprzestrzennych", "2024.12.06")
os.chdir(path)

wektor = "powiaty.gpkg"
powiaty = QgsVectorLayer(wektor, "powiaty", "ogr")

pola = [
    QgsField("ID", QVariant.Int),
    QgsField("centroid_x", QVariant.Double),
    QgsField("centroid_y", QVariant.Double)
]

centroidy = QgsVectorLayer("Point?crs=EPSG:2180", "centroidy", "memory")
provider = centroidy.dataProvider()
provider.addAttributes(pola)
centroidy.updateFields()
nowe_obiekty = []
obiekty = powiaty.getFeatures()

for obiekt in obiekty:
    geometry = obiekt.geometry()
    if geometry.type() == 2:
        centroid = geometry.centroid()
        punkt = centroid.asPoint()
        nowy_obiekt = QgsFeature()
        nowy_obiekt.setGeometry(centroid)
        nowy_obiekt.setAttributes([obiekt.id(), punkt.x(), punkt.y()])
        nowe_obiekty.append(nowy_obiekt)

provider.addFeatures(nowe_obiekty)

sciezka_do_zapisu = "centroidy.gpkg"
QgsVectorFileWriter.writeAsVectorFormat(centroidy, sciezka_do_zapisu, "UTF-8", centroidy.crs(), "GPKG")
