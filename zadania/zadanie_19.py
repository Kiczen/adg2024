from qgis.processing import alg
from qgis.core import QgsVectorLayer, QgsFeature, QgsVectorFileWriter, QgsGeometry

@alg(name = "clip", label = "Clip features by mask layer", group = "examplescripts", group_label = "Example scripts")
@alg.input(type = alg.SOURCE, name = "INPUT", label = "Input vector layer")
@alg.input(type = alg.SOURCE, name = "MASK", label = "Mask vector layer")
@alg.input(type = alg.VECTOR_LAYER_DEST, name = "OUTPUT_PATH", label = "Output path")
@alg.output(type = alg.FILE, name = "OUTPUT", label = "Clipped features")

def clip(instance, parameters, context, feedback, inputs):
    input_layer = instance.parameterAsVectorLayer(parameters, "INPUT", context)
    mask_layer = instance.parameterAsVectorLayer(parameters, "MASK", context)
    output_path = instance.parameterAsOutputLayer(parameters, "OUTPUT_PATH", context)
    crs = input_layer.crs().authid()
    clipped_layer = QgsVectorLayer("Polygon?crs=" + crs, "Clipped", "memory")
    if feedback.isCanceled():
        return {}
    features = []
    for feature in input_layer.getFeatures():
        geom = feature.geometry()
        for mask_feature in mask_layer.getFeatures():
            mask_geom = mask_feature.geometry()
            if geom.intersects(mask_geom):
                clipped_geom = geom.intersection(mask_geom)
                clipped_feature = QgsFeature()
                clipped_feature.setGeometry(clipped_geom)
                features.append(clipped_feature)
        if feedback.isCanceled():
            return {}
    clipped_layer.dataProvider().addFeatures(features)
    clipped_layer.updateExtents()
    if feedback.isCanceled():
        return {}
    QgsVectorFileWriter.writeAsVectorFormatV3(
        layer=clipped_layer,
        fileName=output_path,
        transformContext=context.transformContext(),
        options=QgsVectorFileWriter.SaveVectorOptions()
    )
    return {"OUTPUT": output_path}
