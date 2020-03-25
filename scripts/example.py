# Small example of how this API can be used from python
# Requires matplotlib and descartes packages: pip install -U matplotlib descartes
#
import geopandas
import matplotlib.pyplot as plt
from pathlib import Path

prtr_url = "http://localhost:5000/collections/prtr_emissions/items?startindex=0&limit=500&bundesland=Sachsen&jahr=2017&f=json"
data = geopandas.read_file(prtr_url)

area_url = "http://localhost:5000/collections/districts/items?limit=20&SN_L=14&f=json"
area = geopandas.read_file(area_url)

fig, ax = plt.subplots(figsize=(10, 6))
area.plot(color=None, edgecolor="k", linewidth=2, ax=ax)
data.plot(color="red", ax=ax)

plt.show()
