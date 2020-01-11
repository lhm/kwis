from datapackage import Package
import geopandas
from sqlalchemy import create_engine
import pandas as pd

package = Package('https://datahub.io/lhm/german-prtr-emissions/datapackage.json')
resource = package.get_resource('prtr-emissions-geojson')

df = geopandas.read_file(resource.source)
# Remove entries without geometry
df = df[pd.notnull(df.geometry)]

engine = create_engine('postgresql+psycopg2://docker:docker@localhost:5432/gis')
df.to_postgis(con=engine, name='prtr_emissions', if_exists='replace', index=True, index_label='id')
