
wektor.startEditing()

pole = [QgsField("dlugosc_granicy", QVariant.Double)]
p = wektor.dataProvider()
p.addAttributes(pole)
wektor.updateFields()
i = wektor.fields().indexOf("dlugosc_granicy")

zmiany = {}

for feature in wektor.getFeatures():
    length = feature.geometry().length() / 1000  # Długość w km
    zmiany[feature.id()] = {i: length}

wektor.changeAttributeValues(zmiany)
wektor.commitChanges()
