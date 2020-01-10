import geopandas
from sqlalchemy import create_engine
from pathlib import Path

root = Path(__file__).parents[1]

df = geopandas.read_file(root / 'data/vg250-landkreise.geojson')
# Regions that have sea territories have two entries. For now,
# select only land area in order to get unique records.
df = df[df.GF == 4]

engine = create_engine('postgresql+psycopg2://docker:docker@localhost:5432/gis')
df.to_postgis(con=engine, name='vg250_krs', if_exists='replace')
