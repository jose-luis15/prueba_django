import os
from django.contrib.gis.gdal import DataSource


def parse_departamen_shapefile_to_polygon():
    path_shapefile = os.path.dirname(
        os.path.join(
            os.path.dirname("_file_"), "public/shapefile/DEPARTAMENTO.shp"
        )
    )
    list_layer = DataSource(path_shapefile)[0]
    """
    ['IDDPTO', 'DEPARTAMEN', 'CAPITAL', 'FUENTE']
    """
    field = list_layer.fields  # and layer.geom_type: # noqa
    """
    ['OFTString', 'OFTString', 'OFTString', 'OFTString']
    """
    type_field = [fld.__name__ for fld in list_layer.field_types]  # noqa
    return list_layer
