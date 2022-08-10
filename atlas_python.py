from qgis.core import QgsApplication,QgsProject,QgsLayoutExporter
import os
# inputs
salida = 'C:/Users/user/Downloads/sector/'
layoutname ='ubicacion'
id_mznas_atlas = list(range(8130104001, 8130104012))

# inicar id_mzna, layout
id_mznas = ["{:011d}".format(x) for x in id_mznas_atlas]
qgs = QgsApplication([], True)
qgs.initQgis()
project = QgsProject.instance()
manager = project.layoutManager()
layout = manager.layoutByName(layoutname)

# Exportar
for j in id_mznas:
    salida_sector = salida + j[6:] + '/'
    # crear carpetas de salida
    if not os.path.exists(salida_sector):
        os.makedirs(salida_sector)
    atlas = layout.atlas()
    atlas.setFilterFeatures(True)
    # Filtro atlas
    atlas.setFilterExpression("id_mzna = '%s'" % (j))
    # Iniciar
    atlas.beginRender()
    for i in range(0, atlas.count() + 1):
        # generar JPG
        exporter = QgsLayoutExporter(atlas.layout())
        print('Exportando!!!: '+str(atlas.currentFeatureNumber()) + ' of ' + str(atlas.count()))
        exporter.exportToImage(salida_sector + atlas.currentFilename() + ".JPG", QgsLayoutExporter.ImageExportSettings())
        print('Plano de Ubicacion: '+atlas.currentFilename())
        # crear nuevo layout
        atlas.next()
# Terminar atlas
atlas.endRender()

def buscarJPG(carpeta):
    lista = []
    for ruta, NombreCarpeta, fileNames in os.walk(carpeta):
        for archivo in fileNames:
            if(archivo.startswith('.JPG')):
                lista.append(os.path.join(ruta, archivo))
    return lista
for k in buscarJPG(salida):
    os.remove(k)






