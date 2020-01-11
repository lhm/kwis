from datapackage import Package
import geopandas
from sqlalchemy import create_engine

package = Package('https://raw.githubusercontent.com/lhm/verwaltungsgebiete/master/datapackage.json')
resource = package.get_resource('vg250-districts')

df = geopandas.read_file(resource.source)
# Regions that have sea territories have two entries. For now,
# select only land area in order to get unique records.
df = df[df.GF == 4]

engine = create_engine('postgresql+psycopg2://docker:docker@localhost:5432/gis')
df.to_postgis(con=engine, name='vg250_districts', if_exists='replace')
