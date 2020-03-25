from pandas_datapackage_reader import read_datapackage
import geopandas
from utils import data_dir

df = read_datapackage(
    "https://github.com/lhm/verwaltungsgebiete", resource_name="vg250-districts"
)
# Regions that have sea territories have two entries. For now,
# select only land area in order to get unique records.
df = df[df.GF == 4]

output_path = data_dir / "districts.gpkg"
df.to_file(output_path, layer="districts", driver="GPKG")
