import matplotlib.pyplot as plt


def przeksztalcenia(wkt, typ_transformacji, a=None):
    geometry = QgsGeometry.fromWkt(wkt)
    geom_type = geometry.type()
    vertices = geometry.vertices()
    przeksztalcone = []
    for vertex in vertices:
        if typ_transformacji == 'transpozycja':
            przeksztalcone.append(QgsPointXY(vertex.y(), vertex.x()))
        elif typ_transformacji == 'odbicie_pionowe' and a is not None:
            przeksztalcone.append(QgsPointXY(2 * a - vertex.x(), vertex.y()))
    if geom_type == 0:
        return przeksztalcone
    elif geom_type == 1:
        return QgsGeometry.fromPolylineXY(przeksztalcone)
    elif geom_type == 2:
        return QgsGeometry.fromPolygonXY([przeksztalcone])
    

def geometry_to_coords(geometry):
    if isinstance(geometry, str):
        geometry = QgsGeometry.fromWkt(geometry)
    geom_type = geometry.type()
    coords = []
    if geom_type == 0:
        coords = [geometry.asPoint()]
    elif geom_type == 1:
        coords = geometry.asPolyline()
    elif geom_type == 2:
        coords = geometry.asPolygon()[0]
    return zip(*coords)


poligon = "POLYGON ((40 30, 60 30, 50 40, 40 30))"

transponowane = przeksztalcenia(poligon, 'transpozycja')
odbite_pion = przeksztalcenia(poligon, 'odbicie_pionowe', a=3)

x1, y1 = geometry_to_coords(poligon)
x2, y2 = geometry_to_coords(transponowane)
x3, y3 = geometry_to_coords(odbite_pion)

plt.figure(figsize=(16, 9))
plt.plot(x1, y1, color="blue", zorder=2, label="Oryginalne")
plt.fill(x2, y2, color="red", zorder=2, label="Transpozycja")
plt.fill(x3, y3, color="green", zorder=2, label="Odbicie pionowe")
plt.legend()
plt.show()
