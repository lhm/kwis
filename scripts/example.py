import geopandas
import matplotlib.pyplot as plt
from pathlib import Path

url = "http://localhost:5000/collections/prtr/items?startindex=0&limit=500&bundesland=Sachsen&jahr=2017&f=json"
data = geopandas.read_file(url)
area = geopandas.read_file(Path(__file__).parent / 'landkreise-sn.geojson')

fig, ax = plt.subplots(figsize = (10,6))
area.plot(color=None, edgecolor='k', linewidth = 2, ax=ax)
data.plot(color='red', ax=ax)

plt.show()
