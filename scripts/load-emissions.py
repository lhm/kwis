from pandas_datapackage_reader import read_datapackage
import geopandas
import pandas as pd
from utils import data_dir, root

df = read_datapackage(
    "https://github.com/lhm/schadstoffregister", resource_name="prtr-emissions"
)

gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.geo_long_wgs84, df.geo_lat_wgs84)
)

# Remove entries without geometry
gdf = gdf[pd.notnull(gdf.geometry)]

output_path = data_dir / "prtr_emissions.gpkg"
gdf.to_file(output_path, layer="prtr_emissions", driver="GPKG")
